package com.license.antivirus.notification;

import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Build;

import androidx.core.app.NotificationCompat;
import androidx.core.app.NotificationManagerCompat;

import com.example.antivirus.R;
import com.license.antivirus.scanner.ScanResult;

public class NotificationScanManager {

    private static NotificationScanManager instance;
    private static ManagerState state;
    private static final String CHANNEL_ID = "SCAN_NOTIFICATION";
    private static boolean isCreatedChannel = false;
    private static final int ID_NOTIFICATION_PROGRESS = 123;
    private static final int ID_NOTIFICATION_RESULT = 321;


    private enum ManagerState {
        PROGRESS_SCAN,
        FINISHED_SCAN,
        FIRST_RUN,
    }


    private NotificationScanManager() {
        state = ManagerState.FIRST_RUN;
    }

    public static NotificationScanManager getInstance() {
        if (instance == null) {
            instance = new NotificationScanManager();
        }
        return instance;
    }

    private void createNotificationChannel(Context context) {
        // Create the NotificationChannel, but only on API 26+ because
        // the NotificationChannel class is new and not in the support library
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O && !isCreatedChannel) {
            isCreatedChannel = true;
            CharSequence name = "SCAN_NEW_APP";
            String description = context.getString(R.string.channel_description);
            int importance = android.app.NotificationManager.IMPORTANCE_DEFAULT;
            NotificationChannel channel = new NotificationChannel(CHANNEL_ID, name, importance);
            channel.setDescription(description);
            // Register the channel with the system; you can't change the importance
            // or other notification behaviors after this
            NotificationManager manager = context.getSystemService(NotificationManager.class);
            manager.createNotificationChannel(channel);
        }
    }

    public void setScanInProgressNotification(String packageName, Context context) {
        NotificationManager managerNotification = (NotificationManager) context.getSystemService(Context.NOTIFICATION_SERVICE);
        managerNotification.cancel(ID_NOTIFICATION_RESULT);
        state = ManagerState.PROGRESS_SCAN;
        createNotificationChannel(context);
        NotificationCompat.Builder builder = new NotificationCompat.Builder(context, CHANNEL_ID)
                .setSmallIcon(R.mipmap.logo_antivirus_v2)
                .setContentTitle(context.getString(R.string.new_installed_app))
//                .setContentTitle(packageName)
                .setStyle(new NotificationCompat.BigTextStyle()
                        .bigText(String.format(context.getString(R.string.progress_scan_new_app), packageName)))
                .setPriority(NotificationCompat.PRIORITY_DEFAULT)
                .setAutoCancel(true);
        NotificationManagerCompat notificationManager = NotificationManagerCompat.from(context);
        notificationManager.notify(ID_NOTIFICATION_PROGRESS, builder.build());
    }

    public void setScanResultNotification(String packageName, ScanResult result, Context context) {
        Bitmap resultResource = BitmapFactory.decodeResource(context.getResources(), R.mipmap.warning);
        String message = "";
        switch (result.getLevel()) {
            case Safe:
                resultResource = BitmapFactory.decodeResource(context.getResources(), R.mipmap.safe);
                message = String.format(context.getString(R.string.result_app_safe), packageName);
                break;
            case Warning:
                resultResource = BitmapFactory.decodeResource(context.getResources(), R.mipmap.warning);
                message = String.format(context.getString(R.string.result_app_warning), packageName);
                break;
            case Risky:
                resultResource = BitmapFactory.decodeResource(context.getResources(), R.mipmap.risky);
                message = String.format(context.getString(R.string.result_app_risky), packageName);
                break;
            case Malware:
                resultResource = BitmapFactory.decodeResource(context.getResources(), R.mipmap.malware);
                message = String.format(context.getString(R.string.result_app_malware), packageName);
                break;
        }
        state = ManagerState.FINISHED_SCAN;
        createNotificationChannel(context);
        NotificationManager mNotificationManager = (NotificationManager) context.getSystemService(Context.NOTIFICATION_SERVICE);
        mNotificationManager.cancel(ID_NOTIFICATION_PROGRESS);
        NotificationCompat.Builder builder = new NotificationCompat.Builder(context, CHANNEL_ID)
                .setSmallIcon(R.mipmap.logo_antivirus_v2)
                .setLargeIcon(resultResource)
                .setContentTitle(context.getString(R.string.background_scan_result))
                .setStyle(new NotificationCompat.BigTextStyle().bigText(message))
                .setPriority(NotificationCompat.PRIORITY_DEFAULT)
                .setAutoCancel(true);
        NotificationManagerCompat notificationManager = NotificationManagerCompat.from(context);
        notificationManager.notify(ID_NOTIFICATION_PROGRESS, builder.build());
    }
}
