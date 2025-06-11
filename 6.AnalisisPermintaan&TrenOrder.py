# 6.1 Time Series Jumlah Order per Bulan
plt.figure(figsize=(15, 8))
orders_per_month.plot()
plt.title("Jumlah Order per Bulan")
plt.xlabel("Bulan")
plt.ylabel("Jumlah Order")
plt.grid(True)
plt.tight_layout()
plt.show()

print("Rata-rata jumlah order per bulan:")
print(orders_per_month.describe())

# 6.2 Musiman: Jumlah Order per Bulan & Kuartal
monthly_orders = df_structure['Order_Month'].value_counts().sort_index()

plt.figure(figsize=(10, 5))
monthly_orders.plot(kind='bar', color='orange')
plt.title("Jumlah Order berdasarkan Bulan")
plt.xlabel("Bulan (1=Januari, ..., 12=Desember)")
plt.ylabel("Jumlah Order")
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

print("Jumlah order per bulan:")
print(monthly_orders)

# 6.3 Segmentasi Wilayah: Jumlah Order per Customer State
state_orders = df_structure['Customer State'].value_counts().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 5))
state_orders.plot(kind='bar', color='salmon')
plt.title("Jumlah Order berdasarkan Provinsi (Top 10)")
plt.xlabel("Provinsi")
plt.ylabel("Jumlah Order")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("Top 10 wilayah dengan jumlah order terbanyak:")
print(state_orders)

# 6.4 Produk Paling Banyak Dipesan (berdasarkan Category Name)
product_demand = df_structure['Category Name'].value_counts()

plt.figure(figsize=(20, 10))
product_demand.plot(kind='bar', color='skyblue')
plt.title("Permintaan Berdasarkan Kategori Produk")
plt.xlabel("Kategori")
plt.ylabel("Jumlah Order")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("Jumlah order per kategori produk:")
print(product_demand)
