# 3.1 Proporsi Keterlambatan Secara Umum
late_counts = df_structure['Late_delivery_risk'].value_counts()
late_percentage = df_structure['Late_delivery_risk'].value_counts(normalize=True) * 100

print("Jumlah order berdasarkan keterlambatan:")
print(late_counts)

print("\n Persentase keterlambatan:")
print(late_percentage)

# 3.2 Keterlambatan Berdasarkan Shipping Mode
late_by_shipping = df_structure.groupby('Shipping Mode')['Late_delivery_risk'].mean().sort_values(ascending=False) * 100

print("\n Rata-rata keterlambatan berdasarkan Shipping Mode (dalam %):")
print(late_by_shipping)

# 3.3 Keterlambatan Berdasarkan Customer State
late_by_state = df_structure.groupby('Customer State')['Late_delivery_risk'].mean().sort_values(ascending=False) * 100

print("\n Rata-rata keterlambatan berdasarkan Customer State (dalam %):")
print(late_by_state.head(10))

# 3.4 Keterlambatan Berdasarkan Kategori Produk
late_by_category = df_structure.groupby('Category Name')['Late_delivery_risk'].mean().sort_values(ascending=False) * 100

print("\n Rata-rata keterlambatan berdasarkan Kategori Produk (dalam %):")
print(late_by_category)

# 3.5 Distribusi Keterlambatan Secara Waktu (Bulanan / Tahunan)
df_structure['Order_Year'] = df_structure['order date (DateOrders)'].dt.year
df_structure['Order_Month'] = df_structure['order date (DateOrders)'].dt.month

monthly_late = df_structure.groupby(['Order_Year', 'Order_Month'])['Late_delivery_risk'].mean() * 100

print("\n Persentase keterlambatan per bulan-tahun:")
print(monthly_late.tail(12))
