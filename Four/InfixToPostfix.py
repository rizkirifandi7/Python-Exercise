# Program Konversi Notasi Infix ke Postfix
# I.S. Pengguna memasukkan notasi infix
# F.S. Program menampilkan bentuk notasi postfix dan hasil perhitungan

# Kumpulan operator

Operators = set(['+', '-', '*', '/', '(', ')', '^'])
# Prioritas operator
Prioritas = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


def konversi(ekpresi):
    stack = []  # Inisialiasi stack kosong
    output = ''

    for karakter in ekpresi:
        if (karakter not in Operators):
            output += karakter
        elif (karakter == "("):
            stack.append('(')
        elif (karakter == ")"):
            while stack and stack[-1] != "(":
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != "(" and Prioritas[stack[-1]] >= Prioritas[karakter]:
                output += stack.pop()
            stack.append(karakter)

    while stack:
        output += stack.pop()
    return output


def PerhitunganPostfix(ekpresi):
    stack = []
    output = ''

    for karakter in ekpresi:
        if (karakter not in Operators):
            stack.append(karakter)
        else:
            A = int(stack.pop())
            B = int(stack.pop())

            if (karakter == '+'):
                hasil = B + A
            elif (karakter == '-'):
                hasil = B - A
            elif (karakter == '*'):
                hasil = B * A
            elif (karakter == '/'):
                hasil = B / A
            elif (karakter == '^'):
                hasil = B ** A

            stack.append(hasil)

    while stack:
        output = stack.pop()
    return output


print('--Program Konversi Infix to Postfix--')
ekpresi = input('Masukkan Notasi infix : ')
print('Notasi Postfix : ', konversi(ekpresi))
print('Hasil perhitungan : ', PerhitunganPostfix(konversi(ekpresi)))
