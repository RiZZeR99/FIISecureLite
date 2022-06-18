package com.license.antivirus.scanner;

import android.os.Parcel;
import android.os.Parcelable;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ScanResult implements Parcelable {
    private final ApplicationThreatLevel level;
    private final double permissionsResult;
    private final double receiversResult;
    private final double servicesResult;
    private final List<String> permissionsDetected;
    private final List<String> receiversDetected;
    private final List<String> servicesDetected;
    static Map<String, ApplicationThreatLevel> map;

    static {
        map = new HashMap<String, ApplicationThreatLevel>() {
            {
                put("Safe", ApplicationThreatLevel.Safe);
                put("Warning", ApplicationThreatLevel.Warning);
                put("Risky", ApplicationThreatLevel.Risky);
                put("Malware", ApplicationThreatLevel.Malware);
            }
        };
    }

    public static ScanResult returnDefaultSafe(ApplicationThreatLevel level) {
        return new ScanResult(level, 0, 0, 0,
                new ArrayList(), new ArrayList(), new ArrayList());
    }

    public ScanResult(ApplicationThreatLevel level, double permissionsResult, double receiversResult, double servicesResult, List permissions, List receivers, List services) {
        this.level = level;
        this.permissionsResult = permissionsResult;
        this.receiversResult = receiversResult;
        this.servicesResult = servicesResult;
        permissionsDetected = permissions;
        receiversDetected = receivers;
        servicesDetected = services;
    }

    protected ScanResult(Parcel in) {
        permissionsDetected = new ArrayList<>();
        receiversDetected = new ArrayList<>();
        servicesDetected = new ArrayList<>();

        String levelInString = in.readString();
        level = map.get(levelInString);
        permissionsResult = in.readDouble();
        receiversResult = in.readDouble();
        servicesResult = in.readDouble();

        in.readStringList(permissionsDetected);
        in.readStringList(receiversDetected);
        in.readStringList(servicesDetected);
    }

    public static final Creator<ScanResult> CREATOR = new Creator<ScanResult>() {
        @Override
        public ScanResult createFromParcel(Parcel in) {
            return new ScanResult(in);
        }

        @Override
        public ScanResult[] newArray(int size) {
            return new ScanResult[size];
        }
    };

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel dest, int flags) {
        dest.writeString(level.name());
        dest.writeDouble(permissionsResult);
        dest.writeDouble(receiversResult);
        dest.writeDouble(servicesResult);
        dest.writeStringList(permissionsDetected);
        dest.writeStringList(receiversDetected);
        dest.writeStringList(servicesDetected);
    }

    public ApplicationThreatLevel getLevel() {
        return level;
    }

    public double getPermissionsResult() {
        return permissionsResult;
    }

    public double getReceiversResult() {
        return receiversResult;
    }

    public double getServicesResult() {
        return servicesResult;
    }

    public List<String> getPermissionsDetected() {
        return permissionsDetected;
    }

    public List<String> getReceiversDetected() {
        return receiversDetected;
    }

    public List<String> getServicesDetected() {
        return servicesDetected;
    }
}
