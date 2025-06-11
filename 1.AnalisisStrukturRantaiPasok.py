# 1.1 Cek Struktur Data dan Kolom Terkait
columns_of_interest = [
    'order date (DateOrders)', 'shipping date (DateOrders)', 'Delivery Status',
    'Late_delivery_risk', 'Category Name', 'Customer Segment',
    'Customer State', 'Customer City', 'Shipping Mode'
]

df_structure = df[columns_of_interest].copy()
df_structure.head()

# 1.2 Pastikan Kolom Tanggal dalam Format Datetime
df_structure['order date (DateOrders)'] = pd.to_datetime(df_structure['order date (DateOrders)'])
df_structure['shipping date (DateOrders)'] = pd.to_datetime(df_structure['shipping date (DateOrders)'])
df_structure['Estimated Delivery Date'] = df_structure['shipping date (DateOrders)'] + pd.Timedelta(days=3)

# 1.3 Visualisasi Timeline Aliran Produk
df_structure['Order_to_Ship'] = (df_structure['shipping date (DateOrders)'] - df_structure['order date (DateOrders)']).dt.days
df_structure['Ship_to_Delivery'] = (df_structure['Estimated Delivery Date'] - df_structure['shipping date (DateOrders)']).dt.days
df_structure['Order_to_Delivery'] = (df_structure['Estimated Delivery Date'] - df_structure['order date (DateOrders)']).dt.days

avg_order_to_ship = df_structure['Order_to_Ship'].mean()
avg_ship_to_delivery = df_structure['Ship_to_Delivery'].mean()
avg_total = df_structure['Order_to_Delivery'].mean()

print("\n=== Rata-Rata Waktu Proses ===")
print(f"Rata-rata waktu dari Order ke Shipping: {avg_order_to_ship:.2f} hari")
print(f"Rata-rata waktu dari Shipping ke Delivery: {avg_ship_to_delivery:.2f} hari")
print(f"Total rata-rata waktu dari Order ke Delivery: {avg_total:.2f} hari")

# 1.4 Distribusi Kategori Produk
plt.figure(figsize=(20,10))
sns.countplot(data=df_structure, x='Category Name', order=df_structure['Category Name'].value_counts().index, palette='Set2')
plt.title("Distribusi Kategori Produk", fontsize=14)
plt.xlabel("Kategori Produk", fontsize=12)
plt.ylabel("Jumlah Order", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 1.5 Distribusi Segmentasi & Lokasi Pelanggan
plt.figure(figsize=(8,4))
sns.countplot(data=df_structure, x='Customer Segment', order=df_structure['Customer Segment'].value_counts().index)
plt.title("Segmentasi Pelanggan")
plt.ylabel("Jumlah Order")
plt.show()

top_cities = df_structure['Customer City'].value_counts().head(10)
top_states = df_structure['Customer State'].value_counts().head(10)

plt.figure(figsize=(10,4))
sns.barplot(x=top_cities.index, y=top_cities.values)
plt.title("10 Kota dengan Order Terbanyak")
plt.xticks(rotation=45)
plt.ylabel("Jumlah Order")
plt.show()

plt.figure(figsize=(10,4))
sns.barplot(x=top_states.index, y=top_states.values)
plt.title("10 Negara Bagian dengan Order Terbanyak")
plt.xticks(rotation=45)
plt.ylabel("Jumlah Order")
plt.show()

# 1.6 Distribusi Metode Pengiriman
plt.figure(figsize=(8,4))
sns.countplot(data=df_structure, x='Shipping Mode', order=df_structure['Shipping Mode'].value_counts().index)
plt.title("Distribusi Mode Pengiriman")
plt.ylabel("Jumlah Order")
plt.show()

# 1.7 Ringkasan Per Customer City
city_order_counts = df_structure['Customer City'].value_counts().head(10)

plt.figure(figsize=(12,5))
sns.barplot(x=city_order_counts.index, y=city_order_counts.values, palette="viridis")
plt.title("10 Kota dengan Jumlah Order Tertinggi", fontsize=14)
plt.xlabel("Kota Pelanggan", fontsize=12)
plt.ylabel("Jumlah Order", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

