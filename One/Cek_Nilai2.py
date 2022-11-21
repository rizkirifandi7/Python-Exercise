# pengguna memasukan nilai pada setiap mata pelajaran
ind = int(input("Masukkan nilai Bhs Indonesia : "))
ipa = int(input("Masukkan nilai IPA : "))
mate = int(input("Masukkan nilai Matematika : "))

# menampilkan hasil


def cetak():
    print("Status Keterangan :", status)
    print("Sebab :\n  ", ket)


# validasi apakah nilai di dalam range 0-100
while (ind < 0 or ind > 100) or (ipa < 0 or ipa > 100) or (mate < 0 or mate > 100):
    print("Nilai range yang input adalah 0 - 100!")
    ind = int(input("Masukkan nilai Bhs Indonesia : "))
    ipa = int(input("Masukkan nilai IPA : "))
    mate = int(input("Masukkan nilai Matematika : "))

# proses penentuan lulus tidaknya nilai yang diinput
while True:
    if(ind < 60 and ipa < 60 and mate >= 70):
        status = "TIDAK LULUS"
        ket = "Nilai Bahasa Indonesia kurang dari 60 \n   Nilai IPA kurang dari 60"
        cetak()
        break
    elif(ind >= 60 and ipa < 60 and mate < 70):
        status = "TIDAK LULUS"
        ket = "Nilai IPA kurang dari 60 \n   Nilai Matematika kurang dari 70"
        cetak()
        break
    elif(ind < 60 and ipa >= 60 and mate < 70):
        status = "TIDAK LULUS"
        ket = "Nilai Bahasa Indonesia kurang dari 60 \n   Nilai Matematika kurang dari 70"
        cetak()
        break
    elif(ind < 60 and mate < 70) and (ipa < 60):
        status = "TIDAK LULUS"
        ket = "Nilai Bahasa Indonesia kurang dari 60 \n   Nilai IPA kurang dari 60 \n   Nilai Matematika kurang dari 70"
        cetak()
        break
    elif(ind < 60 and ipa >= 60 and mate >= 70):
        status = "TIDAK LULUS"
        ket = "Nilai Bahasa Indonesia kurang dari 60"
        cetak()
        break
    elif(ind >= 60 and ipa < 60 and mate >= 70):
        status = "TIDAK LULUS"
        ket = "Nilai IPA kurang dari 60"
        cetak()
        break
    elif(ind >= 60 and ipa >= 60 and mate < 70):
        status = "TIDAK LULUS"
        ket = "Nilai Matematika kurang dari 70"
        cetak()
        break
    else:
        status = "LULUS"
        ket = "Semua nilai diatas ketentuan!"
        cetak()
        break
