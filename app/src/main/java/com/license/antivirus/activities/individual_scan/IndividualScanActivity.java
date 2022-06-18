package com.license.antivirus.activities.individual_scan;

import android.content.Intent;
import android.content.pm.ApplicationInfo;
import android.os.Bundle;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.example.antivirus.R;
import com.license.antivirus.activities.interfaces_ui.UILoader;

public class IndividualScanActivity extends AppCompatActivity implements UILoader {

    private IndividualScanLogin controller;
    private TextView textScanApp;


    public IndividualScanActivity(){
        controller = new IndividualScanLogin(this);
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);
        Intent intent = getIntent();
//        controller.scanApp(info);
    }


    @Override
    public void prepareUIComponents() {
        textScanApp = findViewById(R.id.textIndividualScan);
    }
}
