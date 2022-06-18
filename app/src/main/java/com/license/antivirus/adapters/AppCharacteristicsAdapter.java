package com.license.antivirus.adapters;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.example.antivirus.R;

import java.util.ArrayList;
import java.util.List;

public class AppCharacteristicsAdapter extends RecyclerView.Adapter<AppCharacteristicsAdapter.ViewHolder> {
    private final List<String> characteristics = new ArrayList<>();

    public AppCharacteristicsAdapter() {
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.app_list_item_characteristic_scan, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        holder.characteristicTextView.setText(characteristics.get(position));
    }

    @Override
    public int getItemCount() {
        return this.characteristics.size();
    }

    public void setList(List<String> list) {
        this.characteristics.clear();
        this.characteristics.addAll(list);
        notifyDataSetChanged();
    }

    public void addItem(String item) {
        this.characteristics.add(item);
        notifyItemInserted(characteristics.size() - 1);
    }

    public static class ViewHolder extends RecyclerView.ViewHolder {

        private TextView characteristicTextView;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            characteristicTextView = itemView.findViewById(R.id.characteristicApp);
        }
    }

}
