# 📦 Supply Chain Analysis Project

Analisis ini bertujuan untuk mengevaluasi dan memahami berbagai aspek dalam rantai pasok perusahaan e-commerce, dari struktur dasar hingga efisiensi biaya dan pola permintaan.

---

## 📚 About Dataset

Dataset ini digunakan dari **DataCo Global**, berisi data rantai pasok yang kaya fitur untuk keperluan analisis data, machine learning, dan eksplorasi bisnis rantai pasok.

### 🔍 Konten Dataset:
- **Structured Data:** `DataCoSupplyChainDataset.csv`
- **Unstructured Data (opsional):** `tokenized_access_logs.csv` (Clickstream)
- **Deskripsi Kolom:** `DescriptionDataCoSupplyChain.csv`

### 💡 Area Bisnis yang Dicakup:
- Provisioning
- Production
- Sales
- Commercial Distribution

### 🛒 Produk yang Termasuk:
- Clothing
- Sports
- Electronic Supplies

Dataset ini memungkinkan korelasi data terstruktur dan tidak terstruktur untuk menghasilkan wawasan mendalam dalam pengambilan keputusan rantai pasok.

---

## 📄 Data Fields Description

Berikut adalah tabel deskripsi variabel penting dalam dataset:

| **Field**                          | **Description** |
|-----------------------------------|-----------------|
| Type                              | Type of transaction made |
| Days for shipping (real)          | Actual shipping days of the purchased product |
| Days for shipment (scheduled)     | Scheduled delivery days of the purchased product |
| Benefit per order                 | Earnings per order placed |
| Sales per customer                | Total sales made per customer |
| Delivery Status                   | Delivery status: Advance shipping, Late delivery, Canceled, On time |
| Late_delivery_risk                | Indicates if delivery was late (1) or not (0) |
| Category Id                       | Product category code |
| Category Name                     | Description of the product category |
| Customer City                     | City where the customer made the purchase |
| Customer Country                  | Customer's country |
| Customer Email                    | Customer's email |
| Customer Fname                    | Customer's first name |
| Customer Id                       | Unique customer ID |
| Customer Lname                    | Customer's last name |
| Customer Password                 | Encrypted customer password |
| Customer Segment                  | Type of customer: Consumer, Corporate, Home Office |
| Customer State                    | Customer's state |
| Customer Street                   | Customer's street address |
| Customer Zipcode                  | Customer's zip code |
| Department Id                     | Department code of store |
| Department Name                   | Department name of store |
| Latitude                          | Latitude of the store |
| Longitude                         | Longitude of the store |
| Market                            | Market delivered to: Africa, Europe, LATAM, etc. |
| Order City                        | Destination city of the order |
| Order Country                     | Destination country of the order |
| Order Customer Id                 | Customer order code |
| order date (DateOrders)          | Date the order was placed |
| Order Id                          | Unique order code |
| Order Item Cardprod Id           | Product code (RFID-based) |
| Order Item Discount               | Discount value applied |
| Order Item Discount Rate          | Discount rate (percentage) |
| Order Item Id                     | Unique item code |
| Order Item Product Price          | Product price before discount |
| Order Item Profit Ratio           | Profit ratio of item |
| Order Item Quantity               | Quantity per order |
| Sales                             | Sales value |
| Order Item Total                  | Total order value |
| Order Profit Per Order            | Total profit per order |
| Order Region                      | Region where the order is delivered |
| Order State                       | State of delivery |
| Order Status                      | Status: COMPLETE, PENDING, CLOSED, etc. |
| Product Card Id                   | Product code |
| Product Category Id               | Product category code |
| Product Description               | Description of product |
| Product Image                     | Product image link |
| Product Name                      | Name of the product |
| Product Price                     | Final product price |
| Product Status                    | Availability: 1 = not available, 0 = available |
| Shipping date (DateOrders)       | Shipment date & time |
| Shipping Mode                     | Standard Class, First Class, Second Class, Same Day |

---

# 📦 Supply Chain Analysis Project

Analisis ini bertujuan untuk mengevaluasi dan memahami berbagai aspek dalam rantai pasok perusahaan e-commerce, dari struktur dasar hingga efisiensi biaya dan pola permintaan.

---

## 1. 🧩 Analisis Struktur Rantai Pasok

**Tujuan:** Memahami struktur dasar operasional supply chain.

- Menampilkan 5 sample teratas dari dataset.
- Mengidentifikasi tipe data dan deskripsi statistik awal.
- Menampilkan kolom-kolom penting yang tersedia:
  - `order date (DateOrders)`, `shipping date (DateOrders)`, `Delivery Status`, `Shipping Mode`, `Category Name`, dll.

📌 *Insight:* Struktur dataset cukup lengkap untuk analisis end-to-end, namun kolom seperti `vendor` tidak tersedia sehingga harus menyesuaikan analisis selanjutnya.

---

## 2. 📈 Analisis Permintaan & Tren Order

**Tujuan:** Mengetahui tren permintaan produk berdasarkan waktu dan kategori.

### a. Time Series Jumlah Order per Bulan

- Data order di-*resample* per bulan menggunakan `order date (DateOrders)`.
- Visualisasi tren order bulanan menggunakan line chart.

📌 *Insight:* Teridentifikasi lonjakan permintaan pada bulan-bulan tertentu. Ini dapat digunakan untuk menyusun strategi persediaan yang lebih baik.

---

## 3. ⏰ Analisis Keterlambatan Pengiriman

**Tujuan:** Mengukur performa pengiriman dan potensi keterlambatan.

### a. Distribusi Risiko Keterlambatan (`Late_delivery_risk`)
- Visualisasi distribusi keterlambatan pengiriman.
- Analisis status pengiriman (`Delivery Status`) vs risiko keterlambatan.

### b. Shipping Duration per Mode
- Rata-rata durasi pengiriman dihitung berdasarkan `Shipping Mode`.
- Bar chart menunjukkan bahwa semua mode memiliki durasi 3 hari.

📌 *Insight:* Perlu dievaluasi lebih lanjut jika ada penyimpangan per produk atau wilayah.

---

## 4. 🏙️ Analisis Kinerja Berdasarkan Customer City

**Tujuan:** Menilai performa rantai pasok berdasarkan wilayah geografis.

### a. Rata-rata Lead Time dan Shipping Duration per Kota
- Menggunakan kolom `Order_Lead_Time` dan `Shipping_Duration`.
- Kota-kota dengan rata-rata pengiriman lebih lama diidentifikasi.

📌 *Insight:* Beberapa kota mengalami lead time yang jauh lebih tinggi dari rata-rata, potensi untuk perbaikan distribusi regional.

---

## 5. 💰 Analisis Biaya & Efisiensi Keuangan

**Tujuan:** Evaluasi efisiensi finansial dalam operasional supply chain.

### a. Perbandingan Order Total vs Profit
- Scatter plot untuk membandingkan dua metrik (kolom tidak tersedia, maka visualisasi disesuaikan).

### b. Margin Rata-rata Berdasarkan Shipping Mode
- Analisis menggunakan kolom `Shipping Mode` dan `Shipping_Duration`.
- Distribusi profitabilitas berdasarkan metode pengiriman.

📌 *Insight:* Meskipun data keuangan seperti `Order Profit Per Order` atau `Order Item Total` tidak tersedia, dapat digunakan pendekatan alternatif seperti durasi pengiriman dan kategori produk untuk estimasi efisiensi.

---

## 6. 🗓️ Analisis Musiman Permintaan & Kategori Produk

**Tujuan:** Menentukan musim permintaan tinggi dan kategori produk terpopuler.

### a. Jumlah Order berdasarkan Bulan dan Kategori
- Visualisasi menggunakan groupby `Order_Month` dan `Category Name`.
- Bar chart menunjukkan perbedaan volume order antar bulan.

📌 *Insight:* Produk-produk tertentu menunjukkan tren musiman. Ini penting untuk manajemen stok dan kampanye promosi berdasarkan musim.

---

## 📌 Kesimpulan Umum

- **Permintaan** meningkat pada bulan tertentu, terutama untuk kategori produk tertentu.
- **Durasi pengiriman** konsisten, namun perlu perhatian pada kota-kota dengan lead time tinggi.
- **Struktur data** menyediakan fondasi yang baik, meskipun data keuangan lebih lanjut akan memperkuat analisis efisiensi.
- **Rekomendasi:** Implementasi dashboard berbasis wilayah dan musim untuk membantu pengambilan keputusan supply chain secara real-time.

---

## 📊 Tools & Library
- Python (pandas, matplotlib, seaborn)
- Jupyter Notebook
- Dataset dalam format CSV

---

> Created by: *Danang Hilal Kurniawan*
