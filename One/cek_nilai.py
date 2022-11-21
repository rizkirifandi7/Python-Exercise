# pengguna memasukan nilai pada setiap mata pelajaran
ind = int(input("Masukkan nilai Bhs Indonesia : "))
ipa = int(input("Masukkan nilai IPA : "))
mate = int(input("Masukkan nilai Matematika : "))

# validasi apakah nilai dalam range 0-100
while (ind < 0 or ind > 100) or (ipa < 0 or ipa > 100) or (mate < 0 or mate > 100):
    print("Nilai range yang input adalah 0 - 100!")
    ind = int(input("Masukkan nilai Bhs Indonesia : "))
    ipa = int(input("Masukkan nilai IPA : "))
    mate = int(input("Masukkan nilai Matematika : "))

# menentukan lulus/tidak lulus nilai
while True:
    if (ind >= 60 and mate > 70) and (ipa >= 60):
        print("LULUS")
        break
    else:
        print("TIDAK LULUS")
        break
