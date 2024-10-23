# pratek ke-3
# Membuat sebuah sistem restoran sederhana menggunakan OOP
# Interaksi Antar Objek


class MenuItem:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
    def __str__(self):
        return f"{self.nama} - ${self.harga:.2f}"
class Pelanggan:
    def __init__(self, nama):
        self.nama = nama
        self.pesanan = []
    def pesan(self, menu_item):
        self.pesanan.append(menu_item)
        print(f"{self.nama} memesan {menu_item}")
    def bayar(self):
        total = sum(item.harga for item in self.pesanan)
        return total
class Pelayan:
    def __init__(self, nama):
        self.nama = nama
    def ambil_pesanan(self, pelanggan):
        print(f"{self.nama} mengambil pesanan dari{pelanggan.nama}")
    def antar_pesanan(self, pelanggan):
        total = pelanggan.bayar()
        print(f"{self.nama} mengantarkan pesanan kepada {pelanggan.nama}")
        print(f"total tagihan: ${total:.2f}")
class Bayar:
    def __init__(self):
        self.menu = {
            "wdp": MenuItem("wdp", 30,00),
            "dm": MenuItem("dm", 10,00),
            "mdp": MenuItem("mdp", 80,00)
        }
    def siapkan_pesanan(self, pesanan):
        for item in pesanan:
            if item.nama in self.menu:
                print(f"menyediakan {item} dengan harga ${item.harga:.2f}")
            else:
                print(f"{item.nama} tidak ada dalam menu")
            pelanggan = Pelanggan("kurela")
            pelayan = Pelayan("rashford")
            bayar = Bayar()
            wdp = MenuItem("wdp", 30,00)