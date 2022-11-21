nama = input("Masukan nama : ")
gol = input("Masukan golongan [A/B/C/D] : ")


def rumus():
    global gaji_pokok, jum_anak, persen_potongan, gaji_bersih, tunj_anak, tunj_istri
    tunj_istri = 0.1 * gaji_pokok
    tunj_anak = jum_anak * (gaji_pokok * 0.05)

    gaji_kotor = gaji_pokok + tunj_istri + tunj_anak
    gaji_bersih = gaji_kotor - persen_potongan


def cetak():
    if (status == "Menikah") or (status == "menikah"):
        print("=========================================")
        print("      Aplikasi Penggajian Karyawan")
        print("=========================================")
        print("| Nama                   :    ", nama)
        print("| Golongan               :    ", gol)
        print("| Status Pernikahan      :    ", status)
        print("| Jumlah Anak            :    ", jum_anak)
        print("| Gaji Pokok             : Rp.", gaji_pokok)
        print("| Potongan               : Rp.", persen_potongan)
        print("| Tunjangan Anak         : Rp.", tunj_anak)
        print("| Tunjangan Istri        : Rp.", tunj_istri)
        print("|-----------------------------")
        print("| Gaji Bersih            : Rp.", gaji_bersih)
        print("|-----------------------------")
    else:
        print("=========================================")
        print("      Aplikasi Penggajian Karyawan")
        print("=========================================")
        print("| Nama                   :    ", nama)
        print("| Golongan               :    ", gol)
        print("| Status Pernikahan      :    ", status)
        print("| Jumlah Anak            :     -", )
        print("| Gaji Pokok             : Rp.", gaji_pokok)
        print("| Potongan               : Rp.", persen_potongan)
        print("| Tunjangan Anak         : Rp. -")
        print("| Tunjangan Istri        : Rp. -")
        print("|-----------------------------")
        print("| Gaji Bersih            : Rp.", gaji_bersih)
        print("|-----------------------------")


if (gol == "A"):
    status = input("Apakah sudah menikah ? [Menikah/Belum] : ")
    if (status == "Menikah") or (status == "menikah"):
        jum_anak = int(input("Jumlah anak : "))
        gaji_pokok = 10000000
        persen_potongan = 0.025 * gaji_pokok
        rumus()
        cetak()
    else:
        gaji_pokok = 10000000
        persen_potongan = gaji_pokok * 0.025
        gaji_bersih = gaji_pokok - persen_potongan
        cetak()
elif (gol == "B"):
    status = input("Apakah sudah menikah ? [Menikah/Belum] : ")
    if (status == "Menikah") or (status == "menikah"):
        jum_anak = int(input("Jumlah anak : "))
        gaji_pokok = 8500000
        persen_potongan = 0.020 * gaji_pokok
        rumus()
        cetak()
    else:
        gaji_pokok = 8500000
        persen_potongan = gaji_pokok * 0.020
        gaji_bersih = gaji_pokok - persen_potongan
        cetak()
elif (gol == "C"):
    status = input("Apakah sudah menikah ? [Menikah/Belum] : ")
    if (status == "Menikah") or (status == "menikah"):
        jum_anak = int(input("Jumlah anak : "))
        gaji_pokok = 7000000
        persen_potongan = 0.015 * gaji_pokok
        rumus()
        cetak()
    else:
        gaji_pokok = 7000000
        persen_potongan = gaji_pokok * 0.015
        gaji_bersih = gaji_pokok - persen_potongan
        cetak()
elif (gol == "D"):
    status = input("Apakah sudah menikah ? [Menikah/Belum] : ")
    if (status == "Menikah") or (status == "menikah"):
        jum_anak = int(input("Jumlah anak : "))
        gaji_pokok = 5000000
        persen_potongan = 0.010 * gaji_pokok
        rumus()
        cetak()
    else:
        gaji_pokok = 5000000
        persen_potongan = gaji_pokok * 0.010
        gaji_bersih = gaji_pokok - persen_potongan
        cetak()
else:
    print("Golongan tidak ditemukan!")
