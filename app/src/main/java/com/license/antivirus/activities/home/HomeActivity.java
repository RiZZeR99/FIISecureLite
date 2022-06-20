package com.license.antivirus.activities.home;

import android.os.Bundle;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;

import com.example.antivirus.R;
import com.license.antivirus.activities.interfaces_ui.UILoader;

public class HomeActivity extends AppCompatActivity implements UILoader {

    private HomeLogic controller;

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
    }

    public void scanAction(View view) {
        controller.scanDevice(false);
    }

    public void scanFullDevice(View view) {
        controller.scanDevice(true);
    }
}
