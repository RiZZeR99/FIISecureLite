package com.license.antivirus.adapters;

import android.content.Context;
import android.content.Intent;
import android.graphics.BitmapFactory;
import android.os.Parcelable;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.example.antivirus.R;
import com.license.antivirus.activities.report.individual_report.IndividualAppReportActivity;
import com.license.antivirus.adapters.models.ScannedAppInfo;

import java.util.ArrayList;
import java.util.List;

public class AppsScannedAdapter extends RecyclerView.Adapter<AppsScannedAdapter.ViewHolder> {

    private final List<ScannedAppInfo> list = new ArrayList<>();

    public AppsScannedAdapter() {
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.app_list_item_results, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        holder.icon.setImageDrawable(list.get(position).getIcon());
        holder.name.setText(list.get(position).getPackageName());
        holder.info = list.get(position);
        switch (list.get(position).getScanResult().getLevel()) {
            case Safe:
                holder.threatLevel.setImageBitmap(BitmapFactory.decodeResource(holder.threatLevel.getResources(), R.mipmap.safe));
                break;
            case Warning:
                holder.threatLevel.setImageBitmap(BitmapFactory.decodeResource(holder.threatLevel.getResources(), R.mipmap.warning));
                break;
            case Risky:
                holder.threatLevel.setImageBitmap(BitmapFactory.decodeResource(holder.threatLevel.getResources(), R.mipmap.risky));
                break;
            case Malware:
                holder.threatLevel.setImageBitmap(BitmapFactory.decodeResource(holder.threatLevel.getResources(), R.mipmap.malware));
                break;
        }
    }

    @Override
    public int getItemCount() {
        return list.size();
    }

    public void setList(List<ScannedAppInfo> list) {
        this.list.clear();
        this.list.addAll(list);
        notifyDataSetChanged();
    }

    public void addItem(ScannedAppInfo info) {
        this.list.add(info);
        notifyItemInserted(list.size() - 1);
    }

    public static class ViewHolder extends RecyclerView.ViewHolder {

        private final ImageView icon;
        private final TextView name;
        private final ImageView threatLevel;
        private ScannedAppInfo info;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            icon = itemView.findViewById(R.id.appScannedIcon);
            name = itemView.findViewById(R.id.appScannedName);
            threatLevel = itemView.findViewById(R.id.appScannedThreatLevel);
            threatLevel.setOnClickListener(v -> {
                System.out.println(info.getPackageName());
                Context context = itemView.getContext();
                Intent individualReportActivity = new Intent(context, IndividualAppReportActivity.class);
                individualReportActivity.putExtra(context.getString(R.string.individual_app_message), (Parcelable) info);
                itemView.getContext().startActivity(individualReportActivity);
            });

        }
    }
}
