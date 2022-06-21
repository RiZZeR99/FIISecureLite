package com.license.antivirus.activities.scan;

import android.content.Intent;
import android.content.pm.ApplicationInfo;
import android.content.pm.PackageManager;
import android.content.res.AssetFileDescriptor;
import android.graphics.drawable.Drawable;
import android.os.Build;
import android.os.Parcelable;

import androidx.appcompat.content.res.AppCompatResources;

import com.example.antivirus.R;
import com.license.antivirus.activities.home.HomeActivity;
import com.license.antivirus.activities.report.ReportActivity;
import com.license.antivirus.adapters.models.ScannedAppInfo;
import com.license.antivirus.scanner.ApplicationThreatLevel;
import com.license.antivirus.scanner.ScanResult;
import com.license.antivirus.scanner.ScannerApplication;
import com.license.antivirus.utils.ThreadPool;

import org.tensorflow.lite.Interpreter;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.MappedByteBuffer;
import java.nio.channels.FileChannel;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class ScanLogic {

    private final ScanActivity activity;
    private Interpreter modelPermissions;
    private Interpreter modelReceivers;
    private Interpreter modelServices;

    private List<String> permissions;
    private List<String> receivers;
    private List<String> services;

    private volatile boolean scanOn = false;

    public ScanLogic(ScanActivity activity) {
        this.activity = activity;
        scanOn = true;
    }

    private void loadModels() {
        try {
            modelPermissions = new Interpreter(importModelFromAsset("permissions_model.tflite"));
            modelReceivers = new Interpreter(importModelFromAsset("receivers_model.tflite"));
            modelServices = new Interpreter(importModelFromAsset("services_model.tflite"));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private MappedByteBuffer importModelFromAsset(String model) throws IOException {
        AssetFileDescriptor fileDescriptor = activity.getAssets().openFd(model);
        FileInputStream inputStream = new FileInputStream(fileDescriptor.getFileDescriptor());
        FileChannel fileChannel = inputStream.getChannel();
        long startOffset = fileDescriptor.getStartOffset();
        long declaredLength = fileDescriptor.getDeclaredLength();
        return fileChannel.map(FileChannel.MapMode.READ_ONLY, startOffset, declaredLength);
    }

    private void readFile(String fileName) {
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(activity.getAssets().open(fileName)));
            String line;
            while ((line = reader.readLine()) != null) {
                switch (fileName) {
                    case "permissions.txt":
                        permissions.add(line);
                        break;
                    case "receivers.txt":
                        receivers.add(line);
                        break;
                    case "services.txt":
                        services.add(line);
                        break;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void prepareLists() {
        permissions = new ArrayList<>();
        receivers = new ArrayList<>();
        services = new ArrayList<>();
        readFile("permissions.txt");
        readFile("receivers.txt");
        readFile("services.txt");
    }

    void startScanOnDevice(boolean fullScan) {
        ThreadPool.getInstance().execute(() -> {
            scanOn = true;
            PackageManager manager = activity.getPackageManager();
            loadModels();
            prepareLists();
            List<ScannedAppInfo> listScannedApps = new ArrayList<>();
            List<ApplicationInfo> listOfApplication = manager.getInstalledApplications(PackageManager.GET_META_DATA);
            int countApps = listOfApplication.size();
            for (int index = 0; index < countApps && scanOn; index++) {
                if (!listOfApplication.get(index).packageName.toLowerCase().contains(activity.getPackageName())) {
                    if (fullScan) {

                        ScannedAppInfo info = scanApp(listOfApplication.get(index));
                        listScannedApps.add(info);
                        activity.addScannedApp(info);

                    } else if ((listOfApplication.get(index).flags & ApplicationInfo.FLAG_SYSTEM) == 0) { // filtering apps

                        ScannedAppInfo info = scanApp(listOfApplication.get(index));
                        listScannedApps.add(info);
                        activity.addScannedApp(info);
                    }
                }
                activity.setProgressInUI(100 * index / countApps);
            }
            if (scanOn) {
                showReport(listScannedApps);
                scanOn = false;
            }
        });
    }

    private ScannedAppInfo scanApp(ApplicationInfo info) {
        ScannedAppInfo infoScanned;
        try {
            ScannerApplication scanner = new ScannerApplication(info.sourceDir, this.activity, modelPermissions, modelReceivers, modelServices, permissions, receivers, services);
            ScanResult scanResult = scanner.scanApplication();

            Drawable icon = activity.getPackageManager().getApplicationIcon(info.packageName);
            infoScanned = new ScannedAppInfo(icon,
                    info.packageName, scanResult);

        } catch (PackageManager.NameNotFoundException e) {
            e.printStackTrace();
            infoScanned = new ScannedAppInfo(AppCompatResources.getDrawable(activity, R.drawable.ic_launcher_foreground),
                    info.packageName, ScanResult.returnDefaultSafe(ApplicationThreatLevel.Warning));
        }
        System.out.println("App scanned: " + infoScanned.getPackageName() + " Result: " + infoScanned.getScanResult().getLevel().toString());
        System.out.println("Permissions: " + infoScanned.getScanResult().getPermissionsResult() +
                " Receivers: " + infoScanned.getScanResult().getReceiversResult() +
                " Services: " + infoScanned.getScanResult().getServicesResult());
        return infoScanned;
    }

    public void stopScan() {
        scanOn = false;
        Intent scanIntent = new Intent(activity, HomeActivity.class);
        activity.startActivity(scanIntent);
        activity.finish();
    }

    private void showReport(List<ScannedAppInfo> scannedApps) {
        Intent reportIntent = new Intent(activity, ReportActivity.class);
        List<ScannedAppInfo> list = new ArrayList<>();
        for (ScannedAppInfo item : scannedApps) {
            if (item.getScanResult().getLevel() != ApplicationThreatLevel.Safe) {
                list.add(item);
            }
        }
        scannedApps = list;
        reportIntent.putParcelableArrayListExtra(activity.getString(R.string.scannedApps), (ArrayList<? extends Parcelable>) scannedApps);
        activity.startActivity(reportIntent);
        activity.finish();
    }
}
