package com.license.antivirus.activities.report.individual_report;

import android.content.pm.PackageManager;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.content.res.AppCompatResources;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.antivirus.R;
import com.license.antivirus.activities.interfaces_ui.UILoader;
import com.license.antivirus.adapters.AppCharacteristicsAdapter;
import com.license.antivirus.adapters.models.ScannedAppInfo;

public class IndividualAppReportActivity extends AppCompatActivity implements UILoader {

    private ScannedAppInfo info;

    private ImageView icon;
    private ImageView threatLevel;

    private TextView name;
    private TextView permissionsResultScan;
    private TextView receiversResultScan;
    private TextView servicesResultScan;

    private RecyclerView permissionsRecycle;
    private RecyclerView receiversRecycle;
    private RecyclerView servicesRecycle;

    private AppCharacteristicsAdapter adapterPermissions;
    private AppCharacteristicsAdapter adapterReceivers;
    private AppCharacteristicsAdapter adapterServices;

    public IndividualAppReportActivity() {
        adapterPermissions = new AppCharacteristicsAdapter();
        adapterReceivers = new AppCharacteristicsAdapter();
        adapterServices = new AppCharacteristicsAdapter();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_individual_report);
        prepareUIComponents();
    }


    @Override
    public void prepareUIComponents() {
        icon = findViewById(R.id.iconIndividualReport);
        threatLevel = findViewById(R.id.threatLevelImage);
        name = findViewById(R.id.nameAppReport);

        permissionsResultScan = findViewById(R.id.permissionsResultText);
        receiversResultScan = findViewById(R.id.receiversResultText);
        servicesResultScan = findViewById(R.id.servicesResultText);

        permissionsRecycle = findViewById(R.id.recyclerViewPermissions);
        receiversRecycle = findViewById(R.id.recyclerViewReceivers);
        servicesRecycle = findViewById(R.id.recyclerViewServices);

        permissionsRecycle.setLayoutManager(new LinearLayoutManager(this));
        receiversRecycle.setLayoutManager(new LinearLayoutManager(this));
        servicesRecycle.setLayoutManager(new LinearLayoutManager(this));

        permissionsRecycle.setAdapter(adapterPermissions);
        receiversRecycle.setAdapter(adapterReceivers);
        servicesRecycle.setAdapter(adapterServices);

        info = getIntent().getParcelableExtra(getString(R.string.individual_app_message));

        try {
            icon.setImageDrawable(getPackageManager().getApplicationIcon(info.getPackageName()));
        } catch (PackageManager.NameNotFoundException e) {
            icon.setImageDrawable((AppCompatResources.getDrawable(this, R.drawable.ic_launcher_foreground)));
        }
        switch (info.getScanResult().getLevel()) {
            case Safe:
                threatLevel.setImageBitmap(BitmapFactory.decodeResource(getResources(), R.mipmap.safe));
                break;
            case Warning:
                threatLevel.setImageBitmap(BitmapFactory.decodeResource(getResources(), R.mipmap.warning));
                break;
            case Risky:
                threatLevel.setImageBitmap(BitmapFactory.decodeResource(getResources(), R.mipmap.risky));
                break;
            case Malware:
                threatLevel.setImageBitmap(BitmapFactory.decodeResource(getResources(), R.mipmap.malware));
                break;
        }
        name.setText(info.getPackageName());
        permissionsResultScan.setText(String.format(getString(R.string.permissions_result), info.getScanResult().getPermissionsResult()));
        receiversResultScan.setText(String.format(getString(R.string.receivers_result), info.getScanResult().getReceiversResult()));
        servicesResultScan.setText(String.format(getString(R.string.services_result), info.getScanResult().getServicesResult()));

        adapterPermissions.setList(info.getScanResult().getPermissionsDetected());
        adapterReceivers.setList(info.getScanResult().getReceiversDetected());
        adapterServices.setList(info.getScanResult().getServicesDetected());
    }

    public void backFullScanReport(View view) {
        finish();
    }
}
