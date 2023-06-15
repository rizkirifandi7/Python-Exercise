# Class untuk Mahasiswa
class Mahasiswa:
    def __init__(self, nama, nilai):
        self.Nama = nama
        self.Nilai = nilai

# Class untuk Node


class DataMahasiswa:
    def __init__(self, nama, nilai):
        self.info = Mahasiswa(nama, nilai)
        self.next = None


class LinkedList:
    def __init__(self):
        self.awal = None

    # fungsi kososng
    def isEmpty(self):
        return self.awal is None

    # fungsi satu node
    def SatuNode(self):
        bantu = self.awal
        if (bantu.next is None):
            return True
        else:
            return False

    # fungsi tampil data
    def TampilData(self):
        if self.isEmpty():
            print("Data Kosong")
        else:
            bantu = self.awal
            print("------------------------")
            print("|    Nama    |  Nilai  |")
            print("------------------------")
            while (bantu is not None):
                print(bantu.info.Nama, "     ", bantu.info.Nilai,)
                bantu = bantu.next
            print()

    # fungsi buat data baru
    def DataBaru(self):
        nama = str(input("Masukan Nama Mahasiswa : "))
        bantu = self.awal
        while (bantu is not None):
            if (bantu.info.Nama == nama):
                print("Nama Sudah terdaftar, Ulangi")
                nama = str(input("Masukan Nama Mahasiswa :"))
                bantu = self.awal
            else:
                bantu = bantu.next
        nilai = int(input("Masukan Data Nilai Mahasiswa : "))

        return Mahasiswa(nama, nilai)

    # Fungsi tambah depan
    def Tambah(self):
        data = self.DataBaru()
        baru = DataMahasiswa(data.Nama, data.Nilai)
        if (not self.isEmpty()):
            baru.next = self.awal
        self.awal = baru

    # fungsi cari nama
    def CariNama(self):
        if (self.isEmpty()):
            print("Data Kosong")
        else:
            namaCari = str(input("Masukan Nama yang akan dicari :"))
            bantu = self.awal
            ketemu = False
            print("----------------------")
            print("|    Nama    | Nilai |")
            print("----------------------")
            while (bantu is not None):
                if (namaCari in bantu.info.Nama):
                    print(bantu.info.Nama, "     ", bantu.info.Nilai)
                    ketemu = True
                    bantu = bantu.next
                else:
                    bantu = bantu.next
            if (not ketemu):
                print("Nama ", namaCari, " Tidak ditemukan")

    # fungsi cari Nilai
    def CariNilai(self):
        if (self.isEmpty()):
            print("Data Kosong")
        else:
            nilaiCari = int(input("Masukan Nilai yang akan dicari :"))
            bantu = self.awal
            ketemu = False
            print("----------------------")
            print("|    Nama    | Nilai |")
            print("----------------------")
            while (bantu is not None):
                if (nilaiCari == bantu.info.Nilai):
                    print(" ", bantu.info.Nama, "     ", bantu.info.Nilai)
                    ketemu = True
                    bantu = bantu.next
                else:
                    bantu = bantu.next
            if (not ketemu):
                print("Nilai ", nilaiCari, " Tidak ditemukan")


# Algoritma Utama
list = LinkedList()
print("MENU PILIHAN")
print("------------")
print("1. Penambahan Data Mahasiswa")
print("2. Pencarian Data Mahasiswa")
print("3. Tampil Data Mahasiswa")
print("0. Keluar")

pilih1 = int(input("Masukan Menu yang dipilih :"))
while (pilih1 < 0) or (pilih1 > 3):
    print("Menu yang dipilih tidak valid")
    pilih1 = int(input("Masukan Menu yang dipilih :"))
while (pilih1 != 0):
    if (pilih1 == 1):
        print("Penambahan Data Mahasiswa")
        list.Tambah()
    elif (pilih1 == 2):
        print("Pencarian Data Mahasiswa")
        print("-----------------------")
        print("1. Pencarian Nama Tertentu")
        print("2. Pencarian Nilai Tertentu")
        print("0. Kembali")

        pilih2 = int(input("Masukan menu yang dipilih :"))
        while (pilih2 < 0) or (pilih2 > 2):
            print("Menu yang dipilih tidak valid")
            pilih2 = int(input("Masukan Menu yang dipilih :"))
        if (pilih2 == 1):
            print("Pencarian Nama tertentu")
            list.CariNama()
        elif (pilih2 == 2):
            print("Pencarian Nilai Tertentu")
            list.CariNilai()
        else:
            print("Kembali")
    else:
        print("Tampil")
        list.TampilData()

    print("MENU PILIHAN")
    print("------------")
    print("1. Penambahan Data Mahasiswa")
    print("2. Pencarian Data Mahasiswa")
    print("3. Tampil Data Mahasiswa")
    print("0. Keluar")
    pilih1 = int(input("Masukan Menu yang dipilih :"))
    while (pilih1 < 0) or (pilih1 > 3):
        print("Menu yang dipilih tidak valid")
        pilih1 = int(input("Masukan Menu yang dipilih :"))
