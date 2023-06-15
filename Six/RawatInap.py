# Class untuk Pasien
class Pasien:
    def __init__(self, noid, nama, kamar, infus, oksigen, gajiPokok, tambahan, total):
        self.ID = noid
        self.Nama = nama
        self.Kamar = kamar
        self.Infus = infus
        self.Oksigen = oksigen
        self.GajiPokok = gajiPokok
        self.Tambahan = tambahan
        self.Total = total

# Class untuk Node


class DataPasien:
    def __init__(self, noid, nama, kamar, infus, oksigen, gajiPokok, tambahan, total):
        self.info = Pasien(noid, nama, kamar, infus,
                           oksigen, gajiPokok, tambahan, total)
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
            print(
                "----------------------------------------------------------------------------------------------")
            print(
                "|  ID  |    Nama    | Kamar |     Harga     |  Infus  |  Oksigen  | Tambahan |      Total    |")
            print(
                "----------------------------------------------------------------------------------------------")
            while (bantu is not None):
                print(" ", bantu.info.ID, "    ", bantu.info.Nama, "     ", bantu.info.Kamar, "     ",
                      bantu.info.GajiPokok, "         ", bantu.info.Infus, "        ", bantu.info.Oksigen, "      ", bantu.info.Tambahan, "     ", bantu.info.Total)
                bantu = bantu.next
            print()

    # fungsi buat data baru
    def DataBaru(self):
        noid = str(input("Masukan ID Pasien :"))
        bantu = self.awal
        data = self.awal
        while (bantu is not None):
            if (bantu.info.ID == noid):
                print("ID Sudah terdaftar, Ulangi")
                noid = str(input("Masukan ID :"))
                bantu = self.awal
            else:
                bantu = bantu.next
        nama = str(input("Masukan Nama :"))
        kamar = int(input("Masukan Kelas Kamar :"))
        while (kamar < 1) or (kamar > 3):
            print("Kamar Harus antara 1 sampai 3, Ulangi")
            kamar = int(input("Masukan Kamar :"))
        infus = int(input("Jumlah infus :"))
        oksigen = int(input("Jumlah oksigen :"))

        return Pasien(noid, nama, kamar, infus, oksigen, Harga(kamar), Tambahan(infus, oksigen), Total(kamar, infus, oksigen))

    # Fungsi tambah depan
    def TambahDepan(self):
        data = self.DataBaru()
        baru = DataPasien(data.ID, data.Nama, data.Kamar,
                          data.Infus, data.Oksigen, data.GajiPokok, data.Tambahan, data.Total)
        if (not self.isEmpty()):
            baru.next = self.awal
        self.awal = baru

    # fungsi tambah belakang
    def TambahBelakang(self):
        data = self.DataBaru()
        baru = DataPasien(data.ID, data.Nama, data.Kamar, data.Infus, data.Oksigen,
                          data.GajiPokok, data.Tambahan, data.Total)
        if (self.isEmpty()):
            self.awal = baru
        else:
            bantu = self.awal
            while(bantu.next is not None):
                bantu = bantu.next
            bantu.next = baru

    # fungsi tambah tengah
    def TambahTengah(self):
        sisip = int(input("Masukan Posisi sisip :"))
        bantu = self.awal
        posisi = 1
        ketemu = False
        while (not ketemu) and (bantu is not None):
            if (posisi == sisip):
                ketemu = True
            else:
                posisi += 1
                bantu = bantu.next
        if(ketemu):
            if (bantu.next is None):
                self.TambahBelakang()
            else:
                data = self.DataBaru()
                baru = DataPasien(data.ID, data.Nama, data.Kamar, data.Infus, data.Oksigen,
                                  data.GajiPokok, data.Tambahan, data.Total)
                baru.next = bantu.next
                bantu.next = baru
        else:
            print("Data tidak ditemukan")

    # fungsi hapus depan
    def HapusDepan(self):
        if (self.isEmpty()):
            print("Data Kosong")
        else:
            Phapus = self.awal
            if (self.SatuNode()):
                self.awal = None
            else:
                self.awal = Phapus.next
        del Phapus

    # fungsi hapus belakang
    def HapusBelakang(self):
        if (self.isEmpty()):
            print("Data Kosong")
        else:
            Phapus = self.awal
            if (self.SatuNode()):
                self.awal = None
            else:
                while (Phapus.next is not None):
                    Phapus = Phapus.next
                bantu = self.awal
                while (bantu.next != Phapus):
                    bantu = bantu.next
                bantu.next = None
            del Phapus

    # fungsi hapus tengah
    def HapusTengah(self):
        if (self.isEmpty()):
            print("Data kosong")
        else:
            dataHapus = int(input("Data ke berapa yang ingin di hapus :"))
            Phapus = self.awal
            ketemu = False
            posisi = 1
            while (not ketemu) and (Phapus is not None):
                if (posisi == dataHapus):
                    ketemu = True
                else:
                    posisi += 1
                    Phapus = Phapus.next
            if (ketemu):
                if (Phapus == self.awal):
                    self.HapusDepan()
                elif (Phapus.next is None):
                    self.HapusBelakang()
                else:
                    bantu = self.awal
                    while (bantu.next is not Phapus):
                        bantu = bantu.next
                    bantu.next = Phapus.next
                    del Phapus

    # fungsi cari ID
    def CariID(self):
        if(self.isEmpty()):
            print("Data Kosong")
        else:
            idCari = str(input("Masukan ID yang akan di cari :"))
            bantu = self.awal
            ketemu = False
            while (not ketemu) and (bantu is not None):
                if (bantu.info.ID == idCari):
                    print(
                        "----------------------------------------------------------------------------------------------")
                    print(
                        "|  ID  |    Nama    | Kamar |     Harga     |  Infus  |  Oksigen  | Tambahan |      Total    |")
                    print(
                        "----------------------------------------------------------------------------------------------")
                    print(" ", bantu.info.ID, "    ", bantu.info.Nama, "     ", bantu.info.Kamar, "     ",
                          bantu.info.GajiPokok, "     ", bantu.info.Infus, "     ", bantu.info.Oksigen, "     ", bantu.info.Tambahan, "     ", bantu.info.Total)
                    ketemu = True
                else:
                    bantu = bantu.next
            if (not ketemu):
                print("ID ", idCari, "tidak ditemukan")

    # fungsi cari nama
    def CariNama(self):
        if (self.isEmpty()):
            print("Data Kosong")
        else:
            namaCari = str(input("Masukan Nama yang akan dicari :"))
            bantu = self.awal
            ketemu = False
            print(
                "----------------------------------------------------------------------------------------------")
            print(
                "|  ID  |    Nama    | Kamar |     Harga     |  Infus  |  Oksigen  | Tambahan |      Total    |")
            print(
                "----------------------------------------------------------------------------------------------")
            while (bantu is not None):
                if (namaCari in bantu.info.Nama):
                    print(" ", bantu.info.ID, "    ", bantu.info.Nama, "     ", bantu.info.Kamar, "     ",
                          bantu.info.GajiPokok, "     ", bantu.info.Infus, "     ", bantu.info.Oksigen, "     ", bantu.info.Tambahan, "     ", bantu.info.Total)
                    ketemu = True
                    bantu = bantu.next
                else:
                    bantu = bantu.next
            if (not ketemu):
                print("Nama ", namaCari, " Tidak ditemukan")

    # fungsi cari Kamar
    def CariGol(self):
        if (self.isEmpty()):
            print("Data Kosong")
        else:
            golCari = int(input("Masukan Nama yang akan dicari :"))
            bantu = self.awal
            ketemu = False
            print(
                "----------------------------------------------------------------------------------------------")
            print(
                "|  ID  |    Nama    | Kamar |     Harga     |  Infus  |  Oksigen  | Tambahan |      Total    |")
            print(
                "----------------------------------------------------------------------------------------------")
            while (bantu is not None):
                if (bantu.info.Kamar == golCari):
                    print(" ", bantu.info.ID, "    ", bantu.info.Nama, "     ", bantu.info.Kamar, "     ",
                          bantu.info.GajiPokok, "     ", bantu.info.Infus, "     ", bantu.info.Oksigen, "     ", bantu.info.Tambahan, "     ", bantu.info.Total)
                    ketemu = True
                    bantu = bantu.next
                else:
                    bantu = bantu.next
            if (not ketemu):
                print("kamar ", golCari, " Tidak ditemukan")

    # fungsi ubah datas
    def UbahData(self):
        if (self.isEmpty()):
            print("Data Kosong")
        else:
            dataUbah = int(input("Data ke berapa yang ingin di ubah :"))
            bantu = self.awal
            ketemu = False
            posisi = 1
            while (not ketemu) and (bantu is not None):
                if (posisi == dataUbah):
                    ketemu = True
                else:
                    posisi += 1
                    bantu = bantu.next
            if (ketemu):
                data = self.DataBaru()
                bantu.info = data
            else:
                print("Data Ke-", dataUbah, "Tidak ditemukan")

    # fungsi urut data descending maximum sort berdasarkan ID
    def UrutDataDesc(self):
        i = self.awal
        while (i.next is not None):
            max = i
            j = i.next
            while (j is not None):
                if (j.info.ID > max.info.ID):
                    max = j
                j = j.next
            temp = max.info
            max.info = i.info
            i.info = temp

            i = i.next

    # fungsi penghancuran
    def Penghancuran(self):
        Phapus = self.awal
        while (Phapus is not None):
            self.awal = Phapus.next
            del Phapus
            Phapus = self.awal

# fungsi gaji pokok


def Harga(kamar):
    if (kamar == 1):
        return 4000000
    elif (kamar == 2):
        return 3000000
    else:
        return 2000000

# fungsi infus


def Infus(infus):
    jumlahInfus = infus
    hargaInfus = 50000
    return jumlahInfus * hargaInfus

# fungsi infus


def Oksigen(oksigen):
    jumlahOksigen = oksigen
    hargaOksigen = 250000
    return jumlahOksigen * hargaOksigen


# fungsi Tambahan


def Tambahan(infus, oksigen):
    Tambah = Infus(infus) + Oksigen(oksigen)
    return Tambah

# fungsi Gaji bersih


def Total(kamar, infus, oksigen):
    tambahan = Tambahan(infus, oksigen)
    hargaKamar = Harga(kamar)
    return tambahan + hargaKamar


# Algoritma Utama
list = LinkedList()
print("MENU PILIHAN")
print("------------")
print("1. Penambahan Data Pasien")
print("2. Penghapusan Data Pasien")
print("3. Pencarian Data Pasien")
print("4. Pengubahan Data Pasien")
print("5. Tampil Data Pasien")
print("0. Keluar")

pilih1 = int(input("Masukan Menu yang dipilih :"))
while (pilih1 < 0) or (pilih1 > 5):
    print("Menu yang dipilih tidak valid")
    pilih1 = int(input("Masukan Menu yang dipilih :"))
while (pilih1 != 0):
    if (pilih1 == 1):
        print("Penambahan Data Pasien")
        print("-----------------------")
        print("1. Penambahan Data Pasien di Depan")
        print("2. Penambahan Data Pasien di Belakang")
        print("3. Penambahan Data Pasien di Tengah")
        print("0. Kembali")

        pilih2 = int(input("Masukan menu yang dipilih :"))
        while (pilih2 < 0) or (pilih2 > 3):
            print("Menu yang dipilih tidak valid")
            pilih2 = int(input("Masukan Menu yang dipilih :"))
        if (pilih2 == 1):
            print("Penambahan Data Pasien di depan")
            list.TambahDepan()
        elif (pilih2 == 2):
            print("Penambahan Data Pasien di Belakang")
            list.TambahBelakang()
        elif (pilih2 == 3):
            print("Penambahan Data Pasien di Tengah")
            list.TambahTengah()
        else:
            print("Kembali")
    elif (pilih1 == 2):
        print("Penghapusan Data Pasien")
        print("-----------------------")
        print("1. Penghapusan Data Pasien di Depan")
        print("2. Penghapusan Data Pasien di Belakang")
        print("3. Penghapusan Data Pasien di Tengah")
        print("0. Kembali")

        pilih2 = int(input("Masukan menu yang dipilih :"))
        while (pilih2 < 0) or (pilih2 > 3):
            print("Menu yang dipilih tidak valid")
            pilih2 = int(input("Masukan Menu yang dipilih :"))
        if (pilih2 == 1):
            print("Penghapusan Data Pasien di Depan")
            list.HapusDepan()
        elif (pilih2 == 2):
            print("Penghapusan Data Pasien di Belakang")
            list.HapusBelakang()
        elif (pilih2 == 3):
            print("Penghapusan Data Pasien di Tengah")
            list.HapusTengah()
        else:
            print("Kembali")
    elif (pilih1 == 3):
        print("Pencarian Data Pasien")
        print("-----------------------")
        print("1. Pencarian ID Tertentu")
        print("2. Pencarian Nama Tertentu")
        print("3. Pencarian Kamar Tertentu")
        print("0. Kembali")

        pilih2 = int(input("Masukan menu yang dipilih :"))
        while (pilih2 < 0) or (pilih2 > 3):
            print("Menu yang dipilih tidak valid")
            pilih2 = int(input("Masukan Menu yang dipilih :"))
        if (pilih2 == 1):
            print("Pencarian ID Tertentu")
            list.CariID()
        elif (pilih2 == 2):
            print("Pencarian Nama tertentu")
            list.CariNama()
        elif (pilih2 == 3):
            print("Pencarian Kamar Tertentu")
            list.CariGol()
        else:
            print("Kembali")
    elif (pilih1 == 4):
        print("Pengubahan Data Pasien")
        list.UbahData()
    else:
        print("Tampil")
        list.UrutDataDesc()
        list.TampilData()

    print("MENU PILIHAN")
    print("------------")
    print("1. Penambahan Data Pasien")
    print("2. Penghapusan Data Pasien")
    print("3. Pencarian Data Pasien")
    print("4. Pengubahan Data Pasien")
    print("5. Tampil Data Pasien")
    print("0. Keluar")
    pilih1 = int(input("Masukan Menu yang dipilih :"))
    while (pilih1 < 0) or (pilih1 > 5):
        print("Menu yang dipilih tidak valid")
        pilih1 = int(input("Masukan Menu yang dipilih :"))
