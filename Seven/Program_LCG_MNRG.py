class LCG:
    def __init__(self, awal_z, a, c, m):
        self.awal_z = awal_z
        self.a = a
        self.c = c
        self.m = m

    def perhitunganLCG(self):
        count = 1
        while True:
            z = (self.a * self.awal_z + self.c) % self.m
            label = f'Z{count}'

            result = z / self.m
            label1 = f'U{count}'

            yield z, label, label1, self.a, self.awal_z, self.c, self.m, result
            self.awal_z = z
            count += 1

class MNRG:
    def __init__(self, awal_z, a, m):
        self.awal_z = awal_z
        self.a = a
        self.m = m
    def perhitunganMNRG(self):
        count = 1
        while True:
            z = (self.a * self.awal_z) % self.m
            label = f'Z{count}'
            
            result = z / self.m
            label1 = f'U{count}'
            
            yield z, label, label1,self.awal_z, self.a, self.m, result
            self.awal_z = z
            count += 1


# Menu utama
def main_menu():
    print("=== Program Generator Angka Acak ===")
    print("Pilih program:")
    print("1. Linear Congruential Generator (LCG)")
    print("2. Multiply-With-Carry Generator (MNRG)")
    print("0. Keluar")


# Pilihan program LCG
def lcg_menu():
    print("=== Program Linear Congruential Generator (LCG) ===")
    awal_z = int(input("Masukkan nilai awal Z untuk LCG: "))
    a = int(input("Masukkan nilai a untuk LCG: "))
    c = int(input("Masukkan nilai c untuk LCG: "))
    m = int(input("Masukkan nilai mod m untuk LCG: "))

    lcg = LCG(awal_z, a, c, m)
    generator = lcg.perhitunganLCG()

    jum_iterasi = int(input("Masukkan jumlah iterasi: "))

    print("========== Hasil LCG =============")
    for _ in range(jum_iterasi):
        z, label, label1, a, seed, c, m, result = next(generator)
        print(f"{label} = ({a} * {seed} + {c}) mod {m} = {z}")
        print(f"{label1} = {z} / {m} = {result}")
        print("----------------------------------")

# Pilihan program MNRG
def mnrg_menu():
    print("=== Program Multiply-With-Carry Generator (MNRG) ===")
    awal_z = int(input("Masukkan nilai awal benih (seed) untuk MNRG: "))
    a = int(input("Masukkan nilai a untuk MNRG: "))
    m = int(input("Masukkan nilai mod m untuk MNRG: "))
    jum_iterasi = int(input("Masukkan jumlah iterasi: "))

    mnrg = MNRG(awal_z,a,m)
    generator = mnrg.perhitunganMNRG()

    print("========== Hasil MNRG =============")
    for _ in range(jum_iterasi):
        z, label, label1, seed, a, m, result = next(generator)
        print(f"{label} = ({a} * {seed}) mod {m} = {z}")
        print(f"{label1} = {z} / {m} = {result}")
        print("----------------------------------")


# Program utama
while True:
    main_menu()
    choice = input("Masukkan pilihan (0-2): ")

    if choice == '0':
        print("Terima kasih telah menggunakan program ini!")
        break
    elif choice == '1':
        lcg_menu()
    elif choice == '2':
        mnrg_menu()
    else:
        print("Pilihan tidak valid. Silakan pilih angka dari menu (0-2).")
