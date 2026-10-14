# 1. Class induk
class Karyawan:
    def __init__(self, nama, id_karyawan, gaji_pokok):
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.__gaji_pokok = gaji_pokok

    def get_gaji_pokok(self):
        return self.__gaji_pokok

    def set_gaji_pokok(self, gaji):
        if gaji <= 0:
            print("Gaji harus lebih dari 0!")
        else:
            self.__gaji_pokok = gaji

    def hitung_gaji_total(self):
        return self.__gaji_pokok

    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("ID:", self.id_karyawan)
        print("Gaji pokok:", self.get_gaji_pokok())


# 2. Karyawan tetap
class KaryawanTetap(Karyawan):
    def __init__(self, nama, id_karyawan, gaji, tunjangan):
        super().__init__(nama, id_karyawan, gaji)
        self.tunjangan = tunjangan

    def hitung_gaji_total(self):
        return self.get_gaji_pokok() + self.tunjangan

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Tunjangan:", self.tunjangan)
        print("Total gaji:", self.hitung_gaji_total())


# 3. Karyawan kontrak
class KaryawanKontrak(Karyawan):
    def __init__(self, nama, id_karyawan, gaji, jam_lembur, tarif):
        super().__init__(nama, id_karyawan, gaji)
        self.jam_lembur = jam_lembur
        self.tarif = tarif

    def hitung_gaji_total(self):
        return self.get_gaji_pokok() + self.jam_lembur * self.tarif

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Jam lembur:", self.jam_lembur)
        print("Tarif lembur:", self.tarif)
        print("Total gaji:", self.hitung_gaji_total())


# 4. Input karyawan
nama = input("Nama karyawan tetap: ")
id_karyawan = input("ID: ")
gaji = int(input("Gaji pokok: "))
tunjangan = int(input("Tunjangan: "))
tetap = KaryawanTetap(nama, id_karyawan, gaji, tunjangan)

nama = input("\nNama karyawan kontrak: ")
id_karyawan = input("ID: ")
gaji = int(input("Gaji pokok: "))
jam = int(input("Jam lembur: "))
tarif = int(input("Tarif lembur: "))
kontrak = KaryawanKontrak(nama, id_karyawan, gaji, jam, tarif)


# 5. Polymorphism
daftar_karyawan = [tetap, kontrak]

for karyawan in daftar_karyawan:
    print("\n--- Data Karyawan ---")
    karyawan.tampilkan_info()


# 6. Encapsulation
print("\n--- Uji Gaji ---")
tetap.set_gaji_pokok(-1000)
tetap.set_gaji_pokok(4500000)
tetap.tampilkan_info()
