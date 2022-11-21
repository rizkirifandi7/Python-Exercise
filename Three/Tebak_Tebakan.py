import random

angka_rahasia = random.randint(1, 100)

print("Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100.. silahkan tebak ya!!!")

ketemu = False

while not ketemu:
    jawaban = int(input("Tebakan Anda : "))

    if jawaban == angka_rahasia:
        print("Hehehe... Bilangan tebakan anda BENAR :-)")
        ketemu = True
        break
    elif jawaban < angka_rahasia:
        print("Hehehe... Bilangan Tebakan Anda terlalu kecil")

    else:
        print('Hehehe... Bilangan Tebakan Anda terlalu besar')
