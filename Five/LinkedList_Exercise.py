# Class untuk pegawai
class Pegawai:
    def __init__(self, nip, nama, gol, gajiPokok, tunj, gajiBersih):
        self.NIP = nip
        self.Nama = nama
        self.Gol = gol
        self.GajiPokok = gajiPokok
        self.Tunjangan = tunj
        self.GajiBersih = gajiBersih

# Class untuk Node


class DataPegawai:
    def __init__(self, nip, nama, gol, gajiPokok, tunj, gajiBersih):
        self.info = Pegawai(nip, nama, gol, gajiPokok, tunj, gajiBersih)
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
                "------------------------------------------------------------------------")
            print(
                "|  NIP  |    Nama    | Golongan | Gaji Pokok | Tunjangan | Gaji Bersih |")
            print(
                "------------------------------------------------------------------------")
            while (bantu is not None):
                print(" ", bantu.info.NIP, "    ", bantu.info.Nama, "     ", bantu.info.Gol, "     ",
                      bantu.info.GajiPokok, "     ", bantu.info.Tunjangan, "%     ", bantu.info.GajiBersih)
                bantu = bantu.next
            print()

    # fungsi buat data baru
    def DataBaru(self):
        nip = str(input("Masukan NIP :"))
        bantu = self.awal
        data = self.awal
        while (bantu is not None):
            if (bantu.info.NIP == nip):
                print("NIP Sudah terdaftar, Ulangi")
                nip = str(input("Masukan NIP :"))
                bantu = self.awal
            else:
                bantu = bantu.next
        nama = str(input("Masukan Nama :"))
        golongan = int(input("Masukan Golongan :"))
        while (golongan < 1) or (golongan > 3):
            print("Golongan Harus antara 1 sampai 3, Ulangi")
            golongan = int(input("Masukan Golongan :"))

        return Pegawai(nip, nama, golongan, GajiPokok(golongan), Tunjangan(golongan), GajiBersih(golongan))

    # Fungsi tambah depan
    def TambahDepan(self):
        data = self.DataBaru()
        baru = DataPegawai(data.NIP, data.Nama, data.Gol,
                           data.GajiPokok, data.Tunjangan, data.GajiBersih)
        if (not self.isEmpty()):
            baru.next = self.awal
        self.awal = baru

    # fungsi tambah belakang
    def TambahBelakang(self):
        data = self.DataBaru()
        baru = DataPegawai(data.NIP, data.Nama, data.Gol,
                           data.GajiPokok, data.Tunjangan, data.GajiBersih)
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
                baru = DataPegawai(data.NIP, data.Nama, data.Gol,
                                   data.GajiPokok, data.Tunjangan, data.GajiBersih)
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

    # fungsi cari NIP
    def CariNIP(self):
        if(self.isEmpty()):
            print("Data Kosong")
        else:
            nipCari = str(input("Masukan NIP yang akan di cari :"))
            bantu = self.awal
            ketemu = False
            while (not ketemu) and (bantu is not None):
                if (bantu.info.NIP == nipCari):
                    print(
                        "------------------------------------------------------------------------")
                    print(
                        "|  NIP  |    Nama    | Golongan | Gaji Pokok | Tunjangan | Gaji Bersih |")
                    print(
                        "------------------------------------------------------------------------")
                    print(" ", bantu.info.NIP, "    ", bantu.info.Nama, "     ", bantu.info.Gol, "     ",
                          bantu.info.GajiPokok, "     ", bantu.info.Tunjangan, "%     ", bantu.info.GajiBersih)
                    ketemu = True
                else:
                    bantu = bantu.next
            if (not ketemu):
                print("NIP ", nipCari, "tidak ditemukan")

    # fungsi cari nama
    def CariNama(self):
        if (self.isEmpty()):
            print("Data Kosong")
        else:
            namaCari = str(input("Masukan Nama yang akan dicari :"))
            bantu = self.awal
            ketemu = False
            print(
                "------------------------------------------------------------------------")
            print(
                "|  NIP  |    Nama    | Golongan | Gaji Pokok | Tunjangan | Gaji Bersih |")
            print(
                "------------------------------------------------------------------------")
            while (bantu is not None):
                if (namaCari in bantu.info.Nama):
                    print(" ", bantu.info.NIP, "    ", bantu.info.Nama, "     ", bantu.info.Gol, "     ",
                          bantu.info.GajiPokok, "     ", bantu.info.Tunjangan, "%     ", bantu.info.GajiBersih)
                    ketemu = True
                    bantu = bantu.next
                else:
                    bantu = bantu.next
            if (not ketemu):
                print("Nama ", namaCari, " Tidak ditemukan")

    # fungsi cari golongan
    def CariGol(self):
        if (self.isEmpty()):
            print("Data Kosong")
        else:
            golCari = int(input("Masukan Nama yang akan dicari :"))
            bantu = self.awal
            ketemu = False
            print(
                "------------------------------------------------------------------------")
            print(
                "|  NIP  |    Nama    | Golongan | Gaji Pokok | Tunjangan | Gaji Bersih |")
            print(
                "------------------------------------------------------------------------")
            while (bantu is not None):
                if (bantu.info.Gol == golCari):
                    print(" ", bantu.info.NIP, "    ", bantu.info.Nama, "     ", bantu.info.Gol, "     ",
                          bantu.info.GajiPokok, "     ", bantu.info.Tunjangan, "%     ", bantu.info.GajiBersih)
                    ketemu = True
                    bantu = bantu.next
                else:
                    bantu = bantu.next
            if (not ketemu):
                print("golongan ", golCari, " Tidak ditemukan")

    # fungsi ubah data
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

    # fungsi urut data descending maximum sort berdasarkan NIP
    def UrutDataDesc(self):
        i = self.awal
        while (i.next is not None):
            max = i
            j = i.next
            while (j is not None):
                if (j.info.NIP > max.info.NIP):
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


def GajiPokok(golongan):
    if (golongan == 1):
        return 4000000
    elif (golongan == 2):
        return 3000000
    else:
        return 2000000

# fungsi tunjangan


def Tunjangan(golongan):
    if (golongan == 1):
        return 20
    elif (golongan == 2):
        return 15
    else:
        return 10

# fungsi Gaji bersih


def GajiBersih(golongan):
    tunj = GajiPokok(golongan) * Tunjangan(golongan) / 100
    gajiKotor = GajiPokok(golongan) + tunj
    pajak = gajiKotor * 0.05
    return gajiKotor - pajak


# Algoritma Utama
list = LinkedList()
print("MENU PILIHAN")
print("------------")
print("1. Penambahan Data Pegawai")
print("2. Penghapusan Data Pegawai")
print("3. Pencarian Data Pegawai")
print("4. Pengubahan Data Pegawai")
print("5. Tampil Data Pegawai")
print("0. Keluar")

pilih1 = int(input("Masukan Menu yang dipilih :"))
while (pilih1 < 0) or (pilih1 > 5):
    print("Menu yang dipilih tidak valid")
    pilih1 = int(input("Masukan Menu yang dipilih :"))
while (pilih1 != 0):
    if (pilih1 == 1):
        print("Penambahan Data Pegawai")
        print("-----------------------")
        print("1. Penambahan Data Pegawai di Depan")
        print("2. Penambahan Data Pegawai di Belakang")
        print("3. Penambahan Data Pegawai di Tengah")
        print("0. Kembali")

        pilih2 = int(input("Masukan menu yang dipilih :"))
        while (pilih2 < 0) or (pilih2 > 3):
            print("Menu yang dipilih tidak valid")
            pilih2 = int(input("Masukan Menu yang dipilih :"))
        if (pilih2 == 1):
            print("Penambahan Data Pegawai di depan")
            list.TambahDepan()
        elif (pilih2 == 2):
            print("Penambahan Data pegawai di Belakang")
            list.TambahBelakang()
        elif (pilih2 == 3):
            print("Penambahan Data Pegawai di Tengah")
            list.TambahTengah()
        else:
            print("Kembali")
    elif (pilih1 == 2):
        print("Penghapusan Data Pegawai")
        print("-----------------------")
        print("1. Penghapusan Data Pegawai di Depan")
        print("2. Penghapusan Data Pegawai di Belakang")
        print("3. Penghapusan Data Pegawai di Tengah")
        print("0. Kembali")

        pilih2 = int(input("Masukan menu yang dipilih :"))
        while (pilih2 < 0) or (pilih2 > 3):
            print("Menu yang dipilih tidak valid")
            pilih2 = int(input("Masukan Menu yang dipilih :"))
        if (pilih2 == 1):
            print("Penghapusan Data Pegawai di Depan")
            list.HapusDepan()
        elif (pilih2 == 2):
            print("Penghapusan Data Pegawai di Belakang")
            list.HapusBelakang()
        elif (pilih2 == 3):
            print("Penghapusan Data Pegawai di Tengah")
            list.HapusTengah()
        else:
            print("Kembali")
    elif (pilih1 == 3):
        print("Pencarian Data Pegawai")
        print("-----------------------")
        print("1. Pencarian NIP Tertentu")
        print("2. Pencarian Nama Tertentu")
        print("3. Pencarian Golongan Tertentu")
        print("0. Kembali")

        pilih2 = int(input("Masukan menu yang dipilih :"))
        while (pilih2 < 0) or (pilih2 > 3):
            print("Menu yang dipilih tidak valid")
            pilih2 = int(input("Masukan Menu yang dipilih :"))
        if (pilih2 == 1):
            print("Pencarian NIP Tertentu")
            list.CariNIP()
        elif (pilih2 == 2):
            print("Pencarian Nama tertentu")
            list.CariNama()
        elif (pilih2 == 3):
            print("Pencarian Golongan Tertentu")
            list.CariGol()
        else:
            print("Kembali")
    elif (pilih1 == 4):
        print("Pengubahan Data Pegawai")
        list.UbahData()
    else:
        print("Tampil")
        list.UrutDataDesc()
        list.TampilData()

    print("MENU PILIHAN")
    print("------------")
    print("1. Penambahan Data Pegawai")
    print("2. Penghapusan Data Pegawai")
    print("3. Pencarian Data Pegawai")
    print("4. Pengubahan Data Pegawai")
    print("5. Tampil Data Pegawai")
    print("0. Keluar")
    pilih1 = int(input("Masukan Menu yang dipilih :"))
    while (pilih1 < 0) or (pilih1 > 5):
        print("Menu yang dipilih tidak valid")
        pilih1 = int(input("Masukan Menu yang dipilih :"))
