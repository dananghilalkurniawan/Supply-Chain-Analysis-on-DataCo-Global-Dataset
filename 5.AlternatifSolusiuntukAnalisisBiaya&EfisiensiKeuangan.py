# 5. 1 Estimasi Biaya Berdasarkan Shipping Duration & Mode
shipping_cost_proxy = df_structure.groupby('Shipping Mode')['Shipping_Duration'].mean().sort_values(ascending=False)

print("Rata-rata Shipping Duration per Shipping Mode:")
print(shipping_cost_proxy)

plt.figure(figsize=(8, 4))
sns.barplot(x=shipping_cost_proxy.index, y=shipping_cost_proxy.values)
plt.title("Estimasi Durasi Pengiriman per Shipping Mode")
plt.ylabel("Rata-rata Durasi Pengiriman (hari)")
plt.xlabel("Shipping Mode")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# 5.2 Identifikasi Shipping Mode Paling Tidak Efisien
inefficiency_df = df_structure.groupby('Shipping Mode').agg({
    'Shipping_Duration': 'mean',
    'Late_delivery_risk': 'mean'
}).sort_values(by='Late_delivery_risk', ascending=False)

inefficiency_df['Late_delivery_risk (%)'] = inefficiency_df['Late_delivery_risk'] * 100

print("Shipping Mode dengan risiko keterlambatan tinggi dan durasi lama:")
print(inefficiency_df[['Shipping_Duration', 'Late_delivery_risk (%)']])

# 5.3 Margin Efisiensi Berdasarkan Kategori Produk (Proxy Time-Based)
category_efficiency = df_structure.groupby('Category Name')['Total_Lead_Time'].mean().sort_values(ascending=False)

print("Rata-rata Total Lead Time per Kategori Produk:")
print(category_efficiency)

plt.figure(figsize=(20, 10))
sns.barplot(x=category_efficiency.index, y=category_efficiency.values)
plt.title("Rata-rata Total Lead Time per Kategori Produk")
plt.ylabel("Total Lead Time (hari)")
plt.xlabel("Kategori Produk")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()
