# Program Membandingkan Dua Digit NIM

# Input data mahasiswa
nama = input("Nama mahasiswa : ")
nim = input("NIM lengkap    : ")
digit_a = input("Digit A (digit kedua dari belakang): ")
digit_b = input("Digit B (digit terakhir): ")

# Mengubah digit menjadi integer
A = int(digit_a)
B = int(digit_b)

# Menampilkan data mahasiswa
print("\nNama mahasiswa :", nama)
print("NIM lengkap    :", nim)
print("Digit A        :", A)
print("Digit B        :", B)

# Menampilkan hasil perbandingan
print("\n===== HASIL PERBANDINGAN =====")
print("A > B  :", A > B)
print("A < B  :", A < B)
print("A == B :", A == B)
print("A != B :", A != B)
print("A >= B :", A >= B)
print("A <= B :", A <= B)