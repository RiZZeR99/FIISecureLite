package com.license.antivirus.activities.home;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.appcompat.app.AppCompatActivity;

import com.example.antivirus.R;
import com.license.antivirus.activities.interfaces_ui.UILoader;
import com.license.antivirus.scanner.ScanResult;
import com.license.antivirus.scanner.ScannerApplication;
import com.license.antivirus.utils.RealPathUtil;

public class HomeActivity extends AppCompatActivity implements UILoader {

    private HomeLogic controller;
    private ActivityResultLauncher startScanOnApp;

    public HomeActivity() {
        controller = new HomeLogic(this);
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);
        controller.configureDaemonForScan();
    }


    @Override
    public void onBackPressed() {
    }

    @Override
    public void prepareUIComponents() {
        startScanOnApp = registerForActivityResult(new ActivityResultContracts.StartActivityForResult(),
                result -> {
                    if (result.getResultCode() == Activity.RESULT_OK) {

//                        String[] address = {MediaStore.Images.Media.DATA};
//                        assert result.getData() != null;
//                        Cursor cursor = getApplicationContext().getContentResolver().query(result.getData().getData(), null, null, null);
//                        int columnIndex = cursor.getColumnIndexOrThrow(MediaStore.Images.Media.DATA);
//                        cursor.moveToFirst();
//                        cursor.getString(columnIndex);
                        Intent intent = result.getData();
                        if (intent != null) {
//                            int permissionCheck = ContextCompat.checkSelfPermission(this,
//                                    Manifest.permission.READ_EXTERNAL_STORAGE);
//                            if (ContextCompat.checkSelfPermission(this,
//                                    Manifest.permission.WRITE_EXTERNAL_STORAGE)
//                                    != PackageManager.PERMISSION_GRANTED) {
//
//                                if (ActivityCompat.shouldShowRequestPermissionRationale(this,
//                                        Manifest.permission.READ_EXTERNAL_STORAGE)) {
//
//                                } else {
//
//                                    ActivityCompat.requestPermissions(this,
//                                            new String[]{Manifest.permission.READ_EXTERNAL_STORAGE},
//                                            permissionCheck);
//                                }
//                            }
                            String path = RealPathUtil.getRealPath(this, result.getData().getData());
                            ScannerApplication scanner = new ScannerApplication(path, this);

                            ScanResult info = scanner.scanApplication();

                            System.out.println("AYOOO");
                        }
                    }
                });
    }

    public void scanAction(View view) {
        controller.scanDevice(false);
    }

    public void scanFullDevice(View view) {
        controller.scanDevice(true);
    }

    public void scanSpecificApk(View view) {

        Intent intentChooseFile = new Intent(Intent.ACTION_OPEN_DOCUMENT);
        intentChooseFile.setType("*/*");
        Intent choose = Intent.createChooser(intentChooseFile, "Select APK file");

        startScanOnApp.launch(choose);

    }
}
