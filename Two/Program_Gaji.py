nama = input("Masukan nama : ")
gol = input("Masukan golongan [A/B/C/D]: ")


def rumus():
    global gaji_pokok, persen_potongan, gaji_bersih, potongan
    potongan = gaji_pokok * persen_potongan
    gaji_bersih = gaji_pokok - potongan


def cetak():
    print("=========================================")
    print("      Aplikasi Penggajian Karyawan       ")
    print("=========================================")
    print("| Nama                   :    ", nama)
    print("| Golongan               :    ", gol)
    print("| Gaji Pokok             : Rp.", gaji_pokok)
    print("| Potongan               : Rp.", potongan)
    print("|----------------------------------------")
    print("| Gaji Bersih            : Rp.", gaji_bersih)
    print("|----------------------------------------")


if (gol == "A") or (gol == "a"):
    gaji_pokok = 10000000
    persen_potongan = 0.025
    rumus()
    cetak()
elif (gol == "B") or (gol == "b"):
    gaji_pokok = 8500000
    persen_potongan = 0.020
    rumus()
    cetak()
elif (gol == "C") or (gol == "c"):
    gaji_pokok = 7000000
    persen_potongan = 0.015
    rumus()
    cetak()
elif (gol == "D") or (gol == "d"):
    gaji_pokok = 5000000
    persen_potongan = 0.010
    rumus()
    cetak()
else:
    print("Golongan tidak ditemukan!")
