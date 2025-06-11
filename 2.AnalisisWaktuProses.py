# 2.1 Konversi Tanggal
df_structure['order date (DateOrders)'] = pd.to_datetime(df_structure['order date (DateOrders)'])
df_structure['shipping date (DateOrders)'] = pd.to_datetime(df_structure['shipping date (DateOrders)'])
df_structure['Estimated Delivery Date'] = pd.to_datetime(df_structure['Estimated Delivery Date'])

print("Sample hasil konversi kolom tanggal:")
print(df_structure[['order date (DateOrders)', 'shipping date (DateOrders)', 'Estimated Delivery Date']].head())

# 2.2 Hitung Metrik Waktu Proses
df_structure['Order_Lead_Time'] = (df_structure['shipping date (DateOrders)'] - df_structure['order date (DateOrders)']).dt.days
df_structure['Shipping_Duration'] = (df_structure['Estimated Delivery Date'] - df_structure['shipping date (DateOrders)']).dt.days
df_structure['Total_Lead_Time'] = (df_structure['Estimated Delivery Date'] - df_structure['order date (DateOrders)']).dt.days

print("\n Sample hasil perhitungan waktu proses:")
print(df_structure[['Order_Lead_Time', 'Shipping_Duration', 'Total_Lead_Time']].head())

# 2.3 Visualisasi Distribusi Setiap Tahap Proses
plt.figure(figsize=(14,5))
sns.boxplot(data=df_structure[['Order_Lead_Time', 'Shipping_Duration', 'Total_Lead_Time']])
plt.title("Distribusi Waktu Proses (Hari)")
plt.ylabel("Hari")
plt.grid(True)
plt.show()

# 2.4 Statistik Rata-Rata dan Maksimum
print("⏱️ Rata-rata waktu dari Order ke Shipping (Order Lead Time):", df_structure['Order_Lead_Time'].mean(), "hari")
print("⛴️ Rata-rata waktu dari Shipping ke Delivery (Shipping Duration):", df_structure['Shipping_Duration'].mean(), "hari")
print("📦 Rata-rata total waktu dari Order ke Delivery (Total Lead Time):", df_structure['Total_Lead_Time'].mean(), "hari")

print("\n🔝 Maksimum waktu dari Order ke Delivery:", df_structure['Total_Lead_Time'].max(), "hari")

# 2.5 Pola Keterlambatan (Outlier & Korelasi)
threshold = df_structure['Total_Lead_Time'].quantile(0.95)
late_orders = df_structure[df_structure['Total_Lead_Time'] > threshold]
print(f"🔍 Jumlah order yang sangat lama (di atas {threshold:.0f} hari): {late_orders.shape[0]}")

plt.figure(figsize=(10,5))
sns.boxplot(x='Delivery Status', y='Total_Lead_Time', data=df_structure)
plt.title("Lead Time Berdasarkan Status Pengiriman")
plt.xticks(rotation=30)
plt.ylabel("Hari")
plt.grid(True)
plt.show()
