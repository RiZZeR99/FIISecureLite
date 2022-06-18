package com.license.antivirus.adapters.models;

import android.graphics.drawable.Drawable;
import android.os.Parcel;
import android.os.Parcelable;

import com.license.antivirus.scanner.ScanResult;

import java.io.Serializable;

public class ScannedAppInfo implements Parcelable, Serializable {
    private Drawable icon;
    private String packageName;
    private final ScanResult result;

    public ScannedAppInfo(Drawable icon, String packageName, ScanResult result) {
        this.icon = icon;
        this.packageName = packageName;
        this.result = result;
    }

    protected ScannedAppInfo(Parcel in) {
        packageName = in.readString();
        result = in.readParcelable(getClass().getClassLoader());
    }

    public static final Creator<ScannedAppInfo> CREATOR = new Creator<ScannedAppInfo>() {
        @Override
        public ScannedAppInfo createFromParcel(Parcel in) {
            return new ScannedAppInfo(in);
        }

        @Override
        public ScannedAppInfo[] newArray(int size) {
            return new ScannedAppInfo[size];
        }
    };

    public Drawable getIcon() {
        return icon;
    }

    public void setIcon(Drawable icon) {
        this.icon = icon;
    }

    public String getPackageName() {
        return packageName;
    }

    public ScanResult getScanResult() {
        return result;
    }

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel dest, int flags) {
        dest.writeString(packageName);
        dest.writeParcelable(result, flags);
    }
}
