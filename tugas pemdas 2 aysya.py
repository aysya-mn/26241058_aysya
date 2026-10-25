print("================================")
print("      IDENTITAS MAHASISWA")
print("================================")

nama = input("Masukkan nama mahasiswa: ")
nim = int(input("Masukkan NIM: "))
prodi = input("Masukkan program studi: ")
dua_digit_nim = int(input("Masukkan 2 digit terakhir NIM: "))

print("================================")
print("         HASIL PROGRAM")
print("================================")

print("Nama          :", nama)
print("NIM           :", nim)
print("Prodi         :", prodi)
print("2 Digit NIM   :", dua_digit_nim)

print("\nTipe Data Nama:", type(nama))
print("Tipe Data NIM :", type(nim))
print("Tipe Data Prodi:", type(prodi))
print("Tipe Data 2 Digit NIM:", type(dua_digit_nim))
