package com.license.antivirus.broadcasts;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.pm.ApplicationInfo;
import android.content.pm.PackageManager;
import android.os.Build;
import android.widget.Toast;

import androidx.legacy.content.WakefulBroadcastReceiver;

import com.license.antivirus.notification.NotificationScanManager;
import com.license.antivirus.scanner.ApplicationThreatLevel;
import com.license.antivirus.scanner.ScanResult;
import com.license.antivirus.scanner.ScannerApplication;
import com.license.antivirus.utils.ThreadPool;

import java.util.ArrayList;
import java.util.Objects;

public class NewPackageBroadcast extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        if (intent.getData() != null) {
            ApplicationInfo info;
            String packageName = "";
            try {
                packageName = intent.getData().getSchemeSpecificPart();
                info = context.getPackageManager().getApplicationInfo(packageName, 0);
            } catch (PackageManager.NameNotFoundException e) {
                if (!Objects.equals(packageName, "")) {
                    NotificationScanManager.getInstance().setScanResultNotification(packageName,
                            ScanResult.returnDefaultSafe(ApplicationThreatLevel.Warning), context);
                }
                return;
            }
            assert info != null;
            if (filterApp(info, context)) {
                switch (intent.getAction()) {
                    case Intent.ACTION_PACKAGE_ADDED:
                        NotificationScanManager.getInstance().setScanInProgressNotification(packageName, context);

                        ScannerApplication scannerApplication = new ScannerApplication(info.sourceDir, context);
                        ScanResult result = scannerApplication.scanApplication();

                        NotificationScanManager.getInstance().setScanResultNotification(packageName, result, context);
                        break;
                    case Intent.ACTION_PACKAGE_CHANGED://just for debugging tests
                        break;
                }
            }
        }
    }

    private boolean filterApp(ApplicationInfo info, Context context) {
        return (!info.packageName.contains(context.getPackageName())) && ((info.flags & ApplicationInfo.FLAG_SYSTEM) == 0);
    }
}
