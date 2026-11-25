class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.__harga = harga
        self.stok = stok

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, nilai):
        if nilai > 0:
            self.__harga = nilai
        else:
            print("Harga tidak boleh kurang dari 1!")

    def tampilkan(self):
        print(f"{self.nama} | Rp{self.harga:,} | Stok: {self.stok}")


class Kasir:
    jumlah_transaksi = 0

    def __init__(self, nama_kasir):
        self.nama_kasir = nama_kasir
        self.daftar_belanja = []

    def tambah_barang(self, produk, jumlah):
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
        elif jumlah > produk.stok:
            print("Stok tidak mencukupi!")
        else:
            subtotal = produk.harga * jumlah
            self.daftar_belanja.append(
                [produk.nama, jumlah, subtotal]
            )
            produk.stok -= jumlah
            print("Barang berhasil ditambahkan!")

    def hitung_total(self):
        total = 0
        for barang in self.daftar_belanja:
            total += barang[2]
        return total

    @staticmethod
    def hitung_diskon(total):
        if total >= 100000:
            return total * 0.10
        return 0

    @classmethod
    def transaksi_baru(cls):
        cls.jumlah_transaksi += 1
        return cls.jumlah_transaksi

    def cetak_struk(self):
        total = self.hitung_total()
        diskon = self.hitung_diskon(total)
        pembayaran = total - diskon

        print("\n========== STRUK BELANJA ==========")
        print("Kasir:", self.nama_kasir)

        for barang in self.daftar_belanja:
            print(
                barang[0], "x", barang[1],
                "= Rp", format(barang[2], ",.0f")
            )

        print("-----------------------------------")
        print("Total      : Rp", format(total, ",.0f"))
        print("Diskon     : Rp", format(diskon, ",.0f"))
        print("Bayar      : Rp", format(pembayaran, ",.0f"))
        print("===================================")


class Toko:
    def __init__(self):
        self.produk = [
            Produk("Beras", 15000, 20),
            Produk("Minyak", 18000, 15),
            Produk("Gula", 14000, 10),
            Produk("Mie Instan", 3500, 30)
        ]

    def jalankan(self):
        print("===== SISTEM KASIR TOKO =====")
        nama = input("Masukkan nama kasir: ")
        kasir = Kasir(nama)

        while True:
            print("\n===== MENU TOKO =====")
            print("1. Lihat Produk")
            print("2. Tambah Barang")
            print("3. Cetak Struk")
            print("4. Keluar")

            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                print("\nDAFTAR PRODUK:")
                for i, produk in enumerate(self.produk, 1):
                    print(i, end=". ")
                    produk.tampilkan()

            elif pilihan == "2":
                try:
                    nomor = int(input("Nomor produk: "))
                    jumlah = int(input("Jumlah barang: "))

                    if 1 <= nomor <= len(self.produk):
                        kasir.tambah_barang(
                            self.produk[nomor - 1], jumlah
                        )
                    else:
                        print("Produk tidak ditemukan!")

                except ValueError:
                    print("Masukkan angka yang benar!")

            elif pilihan == "3":
                if len(kasir.daftar_belanja) == 0:
                    print("Belum ada barang yang dibeli!")
                else:
                    kasir.cetak_struk()
                    nomor = Kasir.transaksi_baru()
                    print("Nomor transaksi:", nomor)
                    break

            elif pilihan == "4":
                print("Terima kasih!")
                break

            else:
                print("Pilihan tidak valid!")


# PROGRAM UTAMA
toko = Toko()
toko.jalankan()