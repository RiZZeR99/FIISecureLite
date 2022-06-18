package com.license.antivirus.activities.report;

import android.content.Intent;
import android.content.pm.PackageManager;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.content.res.AppCompatResources;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.antivirus.R;
import com.license.antivirus.activities.home.HomeActivity;
import com.license.antivirus.activities.interfaces_ui.UILoader;
import com.license.antivirus.adapters.AppsScannedAdapter;
import com.license.antivirus.adapters.models.ScannedAppInfo;

import java.util.List;

public class ReportActivity extends AppCompatActivity implements UILoader {

    private RecyclerView warningAppsRecycle;
    private RecyclerView riskAppsRecycle;
    private RecyclerView malwareAppsRecycle;
    private TextView warningAppText;
    private TextView riskyAppsText;
    private TextView malwareAppsText;
    private final AppsScannedAdapter adapterWarning;
    private final AppsScannedAdapter adapterRisk;
    private final AppsScannedAdapter adapterMalware;

    public ReportActivity() {
        adapterWarning = new AppsScannedAdapter();
        adapterRisk = new AppsScannedAdapter();
        adapterMalware = new AppsScannedAdapter();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_report);
        prepareUIComponents();
    }

    @Override
    public void onBackPressed() {
        Intent homeIntent = new Intent(this, HomeActivity.class);
        startActivity(homeIntent);
        finish();
    }

    private void displayItems(List<ScannedAppInfo> appsInfo) {
        for (ScannedAppInfo app : appsInfo) {
            switch (app.getScanResult().getLevel()) {
                case Warning:
                    adapterWarning.addItem(app);
                    warningAppsRecycle.smoothScrollToPosition(adapterWarning.getItemCount() - 1);
                    break;
                case Risky:
                    adapterRisk.addItem(app);
                    riskAppsRecycle.smoothScrollToPosition(adapterRisk.getItemCount() - 1);
                    break;
                case Malware:
                    adapterMalware.addItem(app);
                    malwareAppsRecycle.smoothScrollToPosition(adapterMalware.getItemCount() - 1);
                    break;
            }
        }
    }

    private void getIcons(List<ScannedAppInfo> list) {
        for (ScannedAppInfo app : list) {
            try {
                app.setIcon(getPackageManager().getApplicationIcon(app.getPackageName()));
            } catch (PackageManager.NameNotFoundException e) {
                app.setIcon((AppCompatResources.getDrawable(this, R.drawable.ic_launcher_foreground)));
            }
        }
    }

    @Override
    public void prepareUIComponents() {

        warningAppText = findViewById(R.id.warningAppsTitle);
        riskyAppsText = findViewById(R.id.riskyAppsTitle);
        malwareAppsText = findViewById(R.id.malwareAppsTitle);

        warningAppsRecycle = findViewById(R.id.warningAppsRecycle);
        warningAppsRecycle.setAdapter(adapterWarning);
        warningAppsRecycle.setLayoutManager(new LinearLayoutManager(this));

        riskAppsRecycle = findViewById(R.id.riskyAppsRecycle);
        riskAppsRecycle.setAdapter(adapterRisk);
        riskAppsRecycle.setLayoutManager(new LinearLayoutManager(this));

        malwareAppsRecycle = findViewById(R.id.malwareAppsRecycle);
        malwareAppsRecycle.setAdapter(adapterMalware);
        malwareAppsRecycle.setLayoutManager(new LinearLayoutManager(this));

        List<ScannedAppInfo> list = getIntent().getParcelableArrayListExtra(getString(R.string.scannedApps));

        getIcons(list);

        displayItems(list);

        warningAppText.setText(String.format(getString(R.string.warning_apps), adapterWarning.getItemCount()));
        riskyAppsText.setText(String.format(getString(R.string.risky_apps), adapterRisk.getItemCount()));
        malwareAppsText.setText(String.format(getString(R.string.malware_apps), adapterMalware.getItemCount()));
    }

    public void backHome(View view) {
        onBackPressed();
    }
}
