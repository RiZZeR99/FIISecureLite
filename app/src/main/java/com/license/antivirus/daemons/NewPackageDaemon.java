package com.license.antivirus.daemons;

import android.app.Service;
import android.content.BroadcastReceiver;
import android.content.Intent;
import android.content.IntentFilter;
import android.net.ConnectivityManager;
import android.os.IBinder;

import androidx.annotation.Nullable;

import com.license.antivirus.broadcasts.NewPackageBroadcast;

public class NewPackageDaemon extends Service {

    BroadcastReceiver newPackageReceiver;
    private static int ID = 12345;

    @Override
    public void onCreate() {
        super.onCreate();
        registerScanReceiver();
    }

    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    @Override
    public int onStartCommand(Intent intent, int flag, int startId) {
        super.onStartCommand(intent, flag, startId);
        return Service.START_STICKY;
    }

    private void registerScanReceiver() {
        newPackageReceiver = new NewPackageBroadcast();
        IntentFilter filter = new IntentFilter(ConnectivityManager.CONNECTIVITY_ACTION);
        filter.addAction(Intent.ACTION_PACKAGE_ADDED);
        filter.addAction(Intent.ACTION_PACKAGE_CHANGED);
        filter.addDataScheme("package");
        try {
            registerReceiver(newPackageReceiver, filter);
        } catch (Exception e) {
            System.out.println("Already register receiver.");
        }
    }

    @Override
    public void onTaskRemoved(Intent intent) {
    }

    @Override
    public void onDestroy() {
        super.onDestroy();

    }
}
