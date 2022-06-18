package com.license.antivirus.activities.scan;

import android.os.Bundle;
import android.os.Handler;
import android.view.View;
import android.widget.Button;
import android.widget.ProgressBar;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.antivirus.R;
import com.license.antivirus.activities.interfaces_ui.UILoader;
import com.license.antivirus.adapters.AppsScanningAdapter;
import com.license.antivirus.adapters.models.ScannedAppInfo;

import java.util.List;

public class ScanActivity extends AppCompatActivity implements UILoader {

    private final ScanLogic controller;
    private TextView progressNumber;
    private Button backButton;
    private ProgressBar progressBar;
    private final Handler handler;
    private RecyclerView appsScannedRecycleVIew;
    private final AppsScanningAdapter adapter;

    public ScanActivity() {
        controller = new ScanLogic(this);
        handler = new Handler();
        adapter = new AppsScanningAdapter();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_scan);
        prepareUIComponents();
    }

    @Override
    protected void onStart() {
        super.onStart();
    }

    @Override
    protected void onResume() {
        super.onResume();
        controller.startScanOnDevice(getIntent().getBooleanExtra(getString(R.string.fullScanDevice), false));
    }

    void setProgressInUI(int progressValue) {
        handler.post(() -> progressNumber.setText(String.format(getString(R.string.progress), progressValue)));
    }

    void setAppsScannedRecycleVIew(List<ScannedAppInfo> list) {
        handler.post(() -> adapter.setList(list));
    }

    void addScannedApp(ScannedAppInfo info) {
        handler.post(() -> {
            adapter.addItem(info);
            appsScannedRecycleVIew.smoothScrollToPosition(adapter.getItemCount() - 1);
        });
    }

    public void stopScan(View view) {
        controller.stopScan();
        finish();
    }

    @Override
    public void prepareUIComponents() {
        progressNumber = findViewById(R.id.progressNumeric);
        progressBar = findViewById(R.id.progressBarScan);
        backButton = findViewById(R.id.backHome);
        appsScannedRecycleVIew = findViewById(R.id.appsScanned);
        appsScannedRecycleVIew.setAdapter(adapter);
        appsScannedRecycleVIew.setLayoutManager(new LinearLayoutManager(this));
        progressBar.setMax(100);
        setProgressInUI(0);
    }
}