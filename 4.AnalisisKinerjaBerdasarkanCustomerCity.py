# 4.1 Jumlah Order per Kota
city_order_counts = df_structure['Customer City'].value_counts().head(10)

print("10 Kota dengan Jumlah Order Terbanyak:")
print(city_order_counts)

# 4.2 Rata-rata Keterlambatan per Kota
city_delay_rate = df_structure.groupby('Customer City')['Late_delivery_risk'].mean().sort_values(ascending=False).head(10) * 100

print("\n 10 Kota dengan Rata-rata Keterlambatan Tertinggi (%):")
print(city_delay_rate)

# 4.3 Rata-rata Lead Time per Kota
city_lead_time = df_structure.groupby('Customer City')['Total_Lead_Time'].mean().sort_values(ascending=False).head(10)

print("\n 10 Kota dengan Rata-rata Waktu Pengiriman Tertinggi (Total Lead Time):")
print(city_lead_time)
