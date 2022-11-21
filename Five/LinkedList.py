# 1. Pendefinsiian Struktur Data Linked List
# Class Untuk node

class Data :
    def __init__(self, info) :
        self.info = info
        self.next = None

# Class untuk linked list
class LinkedList :
    def __init__(self) -> None:
        self.awal = None

    def isEmpty(self) :
        return self.awal is None

    def TampilData(self) :
        print("Isi Linked List : ", end='')
        if self.isEmpty() :
            print("Data Kosong")
        else:
            bantu = self.awal
            while bantu is not None :
                print(bantu.info,"->",end="")
                if bantu.next is not None :
                    print('->',end='')
                bantu = bantu.next
            print()

    def BanyakNode(self) :
        if self.isEmpty() :
            byknode = 0
        else:
            bantu = self.awal
            byknode = 0 
            while bantu is not None :
                byknode = byknode + 1
                bantu = bantu.next
        return byknode

    def Penghancuran(self) :
        Phapus = self.awal
        while (Phapus is not None) :
            self.awal = Phapus.next
            del Phapus
            Phapus = self.awal

# operasi pencarian data
# pencarian angka
    def PencarianAngka(self) :
        if (self.isEmpty()) :
            print("Data Kosong")
        else:
            CariAngka = int(input("Masukan angka yang dicari : "))
            bantu = self.awal
            ketemu = False
            while (not ketemu) and (bantu is not None) :
                if (bantu.info == CariAngka) :
                    ketemu = True
                else:
                    bantu = bantu.next
            
            if(ketemu) :
                print("Angka",CariAngka,"Ditemukan")
            else :
                print("Angka",CariAngka,"Tidak Ditemukan")

# Pencarian node
    def PencarianNode(self) :
        if (self.isEmpty()) :
            print("Data Kosong")
        else:
            CariNode = int(input("Masukan Node yang dicari : "))
            bantu = self.awal
            ketemu = False
            posisi = 1
            while (not ketemu) and (bantu is not None) :
                if (posisi == CariNode) :
                    ketemu = True
                else:
                    bantu = bantu.next
                    posisi = posisi + 1
            
            if(ketemu) :
                print("Node Ke",CariNode,"Ditemukan")
            else :
                print("Node Ke",CariNode,"Tidak Ditemukan")

# Operasi penambahan
# Penambahan di depan
    def SisipDepanSingle(self, DataBaru) :
        Baru = Node(DataBaru)
        if (not self.isEmpty()) :
            Baru.next = self.awal

        self.awal = Baru 
# Penambahan di belakang
    def SisipBelakangSingle(self,DataBaru) :
        Baru = Node(DataBaru)
        if(self.isEmpty()) :
            print("Data Kosong")
        else:
            bantu = self.awal
            while (bantu.next is not None) :
                bantu = bantu.next
            
            bantu.next = Baru

# Penambahan di tengah (sisip)
    def SisipTengahSingle(self,DataBaru) :
        SisipSetelah = int(input("Sisipkan Setelah : "))
        bantu = self.awal
        ketemu = False
        while (not ketemu) and (bantu is not None) :
            if (bantu.info == SisipSetelah) :
                ketemu = True
            else :
                bantu = bantu.next
        if (ketemu) :
            Baru = Node(DataBaru)
            if(bantu.next is None) :
                self.SisipBelakangSingle(DataBaru)
            else :
                Baru.next = bantu.next
                bantu.next = Baru
        else :
            print("Data",SisipSetelah,"Tidak ditemukan")

# operasi pengubahan data
    def UbahData(self) :
        if(self.isEmpty()) :
            print("Data kosong") 
        else:
            DataUbah = int(input("Masukan Angka yang akan diubah : "))
            bantu = self.awal
            ketemu = False
            while (not ketemu) and (bantu is not None) :
                if (bantu.info == DataUbah) :
                    ketemu = True
                else :
                    bantu = bantu.next
            
            if(ketemu) :
                DataBaru = int(input("Masukkan Data Perubah : "))
                bantu.info = DataBaru
            else:
                print("Data",DataUbah,"Tidak ditemukan")

# operasi penghapusan
    def SatuNode(self) :
        bantu = self.awal
        if(bantu.next is None) :
            return True
        else :
            return False

# penghapusan depan
    def HapusDepanSingle(self) :
        if(self.isEmpty()) :
            print("Data Kosong")
        else:
            Phapus = self.awal
            Elemen = Phapus.info
            if(self.SatuNode()) :
                self.awal = None
            else :
                self.awal = Phapus.next

            del Phapus
            print("Data yang sudah dihapus :",Elemen)

# penghapusan belakang
    def HapusBelakangSingle(self) :
        if(self.isEmpty()) :
            print("Data Kosong")
        else :
            Phapus = self.awal
            if(self.SatuNode()) :
                self.awal = None
            else :
                while(Phapus.next is not None) :
                    Phapus = Phapus.next
                
                bantu = self.awal
                while (bantu.next is not Phapus) :
                    bantu = bantu.next

                bantu.next = None
            
            Elemen = Phapus.info
            del Phapus
            print("Data yang sudah dihapus :",Elemen)

# penghapusan tengah
    def HapusTengahSingle(self) :
        if(self.isEmpty()) :
            print("Data Kosong")
        else :
            DataHapus = int(input("Masukan Angka yang akan dihapus : "))
            Phapus = self.awal
            ketemu = False
            while (not ketemu) and (Phapus is not None) :
                if (Phapus.info == DataHapus) :
                    ketemu = True
                else :
                    Phapus = Phapus.next

            if(ketemu) :
                Elemen = Phapus.info
                if(Phapus == self.awal) :
                    self.HapusDepanSingle()
                elif (Phapus.next is None) :
                    self.HapusBelakangSingle
                else :
                    bantu = self.awal
                    while (bantu.next is not Phapus) :
                        bantu = bantu.next

                    bantu.next = Phapus.next
                    del Phapus
                    print("Data yang sudah dihapus :",Elemen)

# pengurutan data secara ascendung menggunakan minimum sort
    def UrutData(self) :
        i = self.awal
        while (i.next is not None) :
            min = i
            j = i.next
            while (j is not None) :
                if(j.info < min.info) :
                    min = j
                j = j.next

            # proses pertukaran data 
            temp = min.info
            min.info = i.info
            i.info = temp

            # tempatkan i ke simpul berikutnya
            i = i.next


# 2. Inisialilasi Linked List
list1 = LinkedList()
# print("Awal Linked List1 : ",list1.awal)


# 3. Memasukkan Data ke Linked List Secara Langsung
node1 = Data(5)
node2 = Data(7)
node3 = Data(11)
node4 = Data(2)

# print("Isi Node 1 : ",node1.info,"->",node1.next)
# print("Isi Node 2 : ",node2.info,"->",node2.next)

# membuat linked list
list1.awal = node1
node1.next = node2
node2.next = node3
node3.next = node4



# 4. Transversal Untuk Menampilkan Data
list1.TampilData()

# 5. Transversal Untuk Menghitung Banyak Node
# print("Banyak Node Pada List : ",list1.BanyakNode())

# 7. Operasi pencarian data
# list1.PencarianAngka()

# 8. Pencarian node
list1.PencarianNode()

# 9. Penambahan Data
# DataBaru = int(input("Masukan angka yang baru : "))
# Penamabahan di depan
# list1.SisipDepanSingle(DataBaru)
# # penamabahan di belakang
# list1.SisipBelakangSingle(DataBaru)
# penambahan di tengah
# list1.SisipTengahSingle(DataBaru)

# 10. Pengubah data
# list1.UbahData()

# 11. Penghapusan Data
# Penghapusan Ddepan
# list1.HapusDepanSingle()
# pegnhapusan belakang
# list1.HapusBelakangSingle()
# penghapusan tengah
# list1.HapusTengahSingle()

# 12. Pengurutan Data
if (list1.isEmpty()) :
    print("DAta Kosong")
else:
    print("linked list yang sudah terurut")
    list1.UrutData()

list1.TampilData()
# 6. Penghancuran / Penghapusan seluruh Node Linked List
list1.Penghancuran()
# list1.TampilData()
# print("Banyak Node Pada List : ",list1.BanyakNode())