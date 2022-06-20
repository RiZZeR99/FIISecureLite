package com.license.antivirus.activities.home;

import android.content.Intent;
import android.os.Build;

import com.example.antivirus.R;
import com.license.antivirus.activities.scan.ScanActivity;
import com.license.antivirus.daemons.NewPackageDaemon;

public class HomeLogic {

    private final HomeActivity activity;

    public HomeLogic(HomeActivity homeActivity) {
        this.activity = homeActivity;
    }

    public void configureDaemonForScan() {
        Intent intent = new Intent(activity, NewPackageDaemon.class);
        activity.startService(intent);
    }

    public void scanDevice(boolean fullScan) {
        Intent scanIntent = new Intent(activity, ScanActivity.class);
        scanIntent.putExtra(activity.getString(R.string.fullScanDevice), fullScan);
        activity.startActivity(scanIntent);
    }
}
