package com.license.antivirus.scanner;


import android.content.Context;
import android.content.res.AssetFileDescriptor;

import net.dongliu.apk.parser.ApkFile;

import org.tensorflow.lite.Interpreter;
import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.nio.FloatBuffer;
import java.nio.MappedByteBuffer;
import java.nio.channels.FileChannel;
import java.util.ArrayList;
import java.util.List;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

public class ScannerApplication {

    private final String pathApp;
    private final Context context;
    private Interpreter modelPermissions;
    private Interpreter modelReceivers;
    private Interpreter modelServices;
    private List<String> permissionsApp;
    private List<String> receiversApp;
    private List<String> servicesApp;
    private List<String> permissionsList;
    private List<String> receiversList;
    private List<String> servicesList;
    private FloatBuffer inputPermissions;
    private FloatBuffer inputReceivers;
    private FloatBuffer inputServices;
    private final int MAX_PERMISSIONS = 1490;
    private final int MAX_RECEIVERS = 593;
    private final int MAX_SERVICES = 855;
    private final double ponderPermissions = 0.5;
    private final double ponderReceivers = 0.3;
    private final double ponderServices = 0.2;
    private double permissionsResult;
    private double receiversResult;
    private double servicesResult;
    private List<String> permissionsDetected;
    private List<String> receiversDetected;
    private List<String> servicesDetected;

    public ScannerApplication(String pathApp, Context context, Interpreter modelPermissions, Interpreter modelReceivers, Interpreter modelServices, List<String> permissionsList, List<String> receiversList, List<String> servicesList) {
        this.pathApp = pathApp;
        this.context = context;
        this.modelPermissions = modelPermissions;
        this.modelReceivers = modelReceivers;
        this.modelServices = modelServices;
        this.permissionsList = permissionsList;
        this.receiversList = receiversList;
        this.servicesList = servicesList;
    }


    private void loadModels() {
        try {
            modelPermissions = new Interpreter(importModelFromAsset("permissions_model.tflite"));
            modelReceivers = new Interpreter(importModelFromAsset("receivers_model.tflite"));
            modelServices = new Interpreter(importModelFromAsset("services_model.tflite"));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private MappedByteBuffer importModelFromAsset(String model) throws IOException {
        try (AssetFileDescriptor fileDescriptor = context.getAssets().openFd(model)) {
            try (FileInputStream inputStream = new FileInputStream(fileDescriptor.getFileDescriptor())) {
                try (FileChannel fileChannel = inputStream.getChannel()) {
                    long startOffset = fileDescriptor.getStartOffset();
                    long declaredLength = fileDescriptor.getDeclaredLength();
                    return fileChannel.map(FileChannel.MapMode.READ_ONLY, startOffset, declaredLength);
                }

            }
        }
    }

    private void readFile(String fileName) {
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(context.getAssets().open(fileName)));
            String line;
            while ((line = reader.readLine()) != null) {
                switch (fileName) {
                    case "permissions.txt":
                        permissionsList.add(line);
                        break;
                    case "receivers.txt":
                        receiversList.add(line);
                        break;
                    case "services.txt":
                        servicesList.add(line);
                        break;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void prepareLists() {
        permissionsList = new ArrayList<>();
        receiversList = new ArrayList<>();
        servicesList = new ArrayList<>();
        readFile("permissions.txt");
        readFile("receivers.txt");
        readFile("services.txt");
    }

    /**
     * Used only for the new installed apps
     *
     * @param pathApp
     * @param context
     */
    public ScannerApplication(String pathApp, Context context) {
        this.pathApp = pathApp;
        this.context = context;
        loadModels();
        prepareLists();
    }


    public ScanResult scanApplication() {
        ScanResult scanResult = ScanResult.returnDefaultSafe(ApplicationThreatLevel.Safe);
        permissionsDetected = new ArrayList<>();
        receiversDetected = new ArrayList<>();
        servicesDetected = new ArrayList<>();
        try {
            obtainMLAttributes();
            buildAttributesArray();

            permissionsResult = runPermissionsModel();
            receiversResult = runReceiversModel();
            servicesResult = runServicesModel();

            ApplicationThreatLevel classificationLevel = computeSafeLevel(permissionsResult * ponderPermissions, receiversResult * ponderReceivers, servicesResult * ponderServices);
            scanResult = new ScanResult(classificationLevel,
                    permissionsResult, receiversResult, servicesResult,
                    permissionsDetected, receiversDetected, servicesDetected);

        } catch (IOException | ParserConfigurationException | SAXException e) {
            System.out.println("Exception occurred when analyzing the app");
            scanResult = ScanResult.returnDefaultSafe(ApplicationThreatLevel.Warning);
            e.printStackTrace();
        }
        return scanResult;
    }

    private void obtainMLAttributes() throws IOException, ParserConfigurationException, SAXException {
        ApkFile program = new ApkFile(pathApp);

        permissionsApp = program.getApkMeta().getUsesPermissions(); // getting the list of permissions
        receiversApp = new ArrayList<>();
        servicesApp = new ArrayList<>();

        String manifest = program.getManifestXml();
        DocumentBuilder builder = DocumentBuilderFactory.newInstance().newDocumentBuilder();
        InputSource xmlSource = new InputSource();
        xmlSource.setCharacterStream(new StringReader(manifest));
        Document xmlDocument = builder.parse(xmlSource);

        Node applicationNode = xmlDocument.getElementsByTagName("application").item(0);
        for (int i = 0; i < applicationNode.getChildNodes().getLength(); i++) {
            Node node = applicationNode.getChildNodes().item(i);
            if (node.getNodeName().contains("receiver")) {
                receiversApp.add(node.getAttributes().getNamedItem("android:name").getNodeValue());//getting the exact receiver used
            } else if (node.getNodeName().contains("service")) {
                servicesApp.add(node.getAttributes().getNamedItem("android:name").getNodeValue());//getting the exact service used
            }
        }
    }

    private void buildAttributesArray() {
        inputPermissions = FloatBuffer.allocate(MAX_PERMISSIONS);
        inputReceivers = FloatBuffer.allocate(MAX_RECEIVERS);
        inputServices = FloatBuffer.allocate(MAX_SERVICES);

        for (int i = 0, j = 0, k = 0; i < MAX_PERMISSIONS || j < MAX_RECEIVERS || k < MAX_SERVICES; i++, j++, k++) {
            analyzeAttributeOfApplication(inputPermissions, i, MAX_PERMISSIONS, permissionsApp, permissionsList, permissionsDetected);
            analyzeAttributeOfApplication(inputReceivers, j, MAX_RECEIVERS, receiversApp, receiversList, receiversDetected);
            analyzeAttributeOfApplication(inputServices, k, MAX_SERVICES, servicesApp, servicesList, servicesDetected);
        }
    }

    private void analyzeAttributeOfApplication(FloatBuffer buffer, int index, int upperLimit, List<String> appCharacteristics, List<String> characteristics, List<String> characteristicDetected) {
        //the buffer must have the values in the exact order like the characteristic list in order for the model to predict it correctly
        if (index < upperLimit) {
            buffer.array()[index] = 0;
            for (String appCharacteristic : appCharacteristics) {
                if (appCharacteristic.endsWith(characteristics.get(index))) {
                    buffer.array()[index] = 1;
                    characteristicDetected.add(appCharacteristic);
                    break;
                }
            }
        }
    }

    private int checkInputToHaveData(FloatBuffer buffer) {
        int sum = 0;
        for (int i = 0; i < buffer.array().length; i++) {
            sum += (int) buffer.array()[i];
        }
        return sum;
    }

    private double runPermissionsModel() {
        if (!permissionsApp.isEmpty()) {
            FloatBuffer outputPermissions = FloatBuffer.allocate(MAX_PERMISSIONS);
            modelPermissions.run(inputPermissions, outputPermissions);
            return outputPermissions.array()[0];
        }
        return 0;
    }

    private double runReceiversModel() {
        if (!receiversApp.isEmpty()) {
            FloatBuffer outputReceivers = FloatBuffer.allocate(MAX_RECEIVERS);
            modelReceivers.run(inputReceivers, outputReceivers);
            return outputReceivers.array()[0];
        }
        return 0;
    }

    private double runServicesModel() {
        if (!servicesApp.isEmpty()) {
            FloatBuffer outputServices = FloatBuffer.allocate(MAX_SERVICES);
            modelServices.run(inputServices, outputServices);
            return outputServices.array()[0];
        }
        return 0;
    }

    private ApplicationThreatLevel computeSafeLevel(double permissionsResult, double receiversResult, double servicesResult) {
        /**
         * Scales
         * 0-0.4 -> safe
         * 0.41-0.6 -> unknown
         * 0.61-0.8 -> risky
         * 0.81 - 1 -> malware
         */

        double score = permissionsResult + receiversResult + servicesResult;
        if (score <= 0.4) {
            return ApplicationThreatLevel.Safe;
        }
        if (score <= 0.6) {
            return ApplicationThreatLevel.Warning;
        }
        if (score <= 0.8) {
            return ApplicationThreatLevel.Risky;
        }
        return ApplicationThreatLevel.Malware;
    }
}
