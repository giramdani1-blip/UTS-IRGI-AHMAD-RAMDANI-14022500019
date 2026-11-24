class Mahasiswa:
    nim = 0
    nama = ""

    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim


mhs = Mahasiswa("Max Verstappen", "12345678")

print("Nama :", mhs.nama)
print("NIM :", mhs.nim)
