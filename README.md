# 🛒 Sistem Kasir Toko – Python OOP

## Deskripsi Project
Sistem Kasir Toko merupakan program sederhana berbasis Python yang digunakan untuk mengelola transaksi pembelian barang di sebuah toko. Program ini dibuat dengan menerapkan konsep Object-Oriented Programming (OOP) untuk mengelola produk, proses pembelian, perhitungan total harga, pemberian diskon, serta pencetakan struk belanja.

Program dijalankan melalui terminal dan tidak menggunakan database. Data produk sudah tersedia di dalam program.

## Fitur Program
- Menampilkan daftar produk beserta harga dan stok.
- Menambahkan barang ke daftar belanja.
- Memvalidasi jumlah pembelian.
- Mengecek ketersediaan stok barang.
- Menghitung subtotal dan total belanja.
- Memberikan diskon 10% jika total belanja mencapai Rp100.000 atau lebih.
- Mencetak struk belanja.
- Menghasilkan nomor transaksi.
- Mengurangi stok barang setelah pembelian berhasil.

## Daftar Produk
Produk yang tersedia di dalam program:

| Nama Produk | Harga | Stok |
|---|---:|---:|
| Beras | Rp15.000 | 20 |
| Minyak | Rp18.000 | 15 |
| Gula | Rp14.000 | 10 |
| Mie Instan | Rp3.500 | 30 |

## Konsep Object-Oriented Programming (OOP)

### 1. Class
Program ini memiliki tiga class utama:

- **Produk**: Mengelola nama, harga, dan stok barang.
- **Kasir**: Mengelola proses pembelian, perhitungan total, diskon, dan struk transaksi.
- **Toko**: Mengelola daftar produk dan menu utama program.

### 2. Object
Object dibuat dari class yang telah didefinisikan. Contohnya, object produk berupa Beras, Minyak, Gula, dan Mie Instan, serta object kasir yang digunakan untuk menjalankan transaksi.

### 3. Constructor (`__init__`)
Constructor digunakan untuk memberikan nilai awal pada object ketika object dibuat.

Pada class Produk, constructor digunakan untuk menyimpan nama produk, harga, dan stok. Pada class Kasir, constructor digunakan untuk menyimpan nama kasir dan membuat daftar belanja. Pada class Toko, constructor digunakan untuk menyediakan daftar produk.

### 4. Attribute dan Method
Attribute merupakan data yang dimiliki oleh object, seperti nama produk, harga, stok, dan nama kasir.

Method merupakan fungsi yang berada di dalam class, seperti `tambah_barang()`, `hitung_total()`, `hitung_diskon()`, `cetak_struk()`, dan `jalankan()`.

### 5. Encapsulation
Encapsulation diterapkan pada attribute harga di class Produk menggunakan attribute privat `__harga`. Attribute tersebut tidak diubah secara langsung, tetapi melalui property dan setter sehingga perubahan harga dapat dikontrol.

### 6. Property dan Setter
Property digunakan untuk membaca nilai harga melalui `@property`, sedangkan setter menggunakan `@harga.setter` untuk mengatur harga baru.

Setter dilengkapi validasi agar harga tidak boleh kurang dari 1. Jika harga tidak memenuhi ketentuan, program akan menampilkan pesan kesalahan.

### 7. Class Method
Class method diterapkan pada method `transaksi_baru()` menggunakan decorator `@classmethod`.

Method ini berfungsi untuk menambah jumlah transaksi dan menghasilkan nomor transaksi baru dengan memanfaatkan attribute class `jumlah_transaksi`.

### 8. Static Method
Static method diterapkan pada method `hitung_diskon()` menggunakan decorator `@staticmethod`.

Method ini digunakan untuk menghitung diskon tanpa bergantung pada object maupun class secara langsung. Jika total belanja mencapai Rp100.000, pelanggan mendapatkan diskon sebesar 10%. Jika kurang dari Rp100.000, maka tidak ada diskon.

## Alur Kerja Program
1. Program dijalankan dan menampilkan menu toko.
2. Pengguna memasukkan nama kasir.
3. Pengguna dapat melihat daftar produk.
4. Pengguna memilih produk dan memasukkan jumlah pembelian.
5. Program memeriksa jumlah pembelian dan ketersediaan stok.
6. Jika valid, barang dimasukkan ke daftar belanja dan stok dikurangi.
7. Pengguna memilih cetak struk.
8. Program menghitung total belanja dan diskon.
9. Struk ditampilkan beserta nomor transaksi.
10. Program selesai.

## Teknologi yang Digunakan
- Python
- Object-Oriented Programming (OOP)
- Terminal / Command Line Interface (CLI)

## Cara Menjalankan Program
1. Pastikan Python sudah terinstal di komputer.
2. Download atau clone repository ini.
3. Buka folder project melalui Visual Studio Code.
4. Buka terminal.
5. Jalankan perintah:

```bash
python deren.py
```

## Tujuan Project
Project ini dibuat sebagai latihan penerapan konsep Object-Oriented Programming (OOP) dalam bahasa Python, sekaligus memahami bagaimana class, object, encapsulation, property, setter, class method, dan static method digunakan dalam sebuah program sederhana yang memiliki fungsi nyata.

---

**Dib