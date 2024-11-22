# Program untuk menambahkan data ke dalam list dan menghitung nilai akhir

# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

# Fungsi untuk menampilkan data
def tampilkan_data(data_list):
    print("\nDaftar Data:")
    print("=" * 60)
    print(f"{'No':<3} {'Nama':<15} {'NIM':<10} {'Tugas':<6} {'UTS':<6} {'UAS':<6} {'Nilai Akhir':<12}")
    print("=" * 60)
    for i, data in enumerate(data_list, start=1):
        print(f"{i:<3} {data['Nama']:<15} {data['NIM']:<10} {data['Tugas']:<6.1f} {data['UTS']:<6.1f} {data['UAS']:<6.1f} {data['Nilai Akhir']:<12.1f}")
    print("=" * 60)

# List untuk menyimpan data
data_list = []

# Perulangan untuk input data
while True:
    nama = input("Masukkan nama: ")
    nim = input("Masukkan NIM: ")
    tugas = float(input("Masukkan nilai tugas (0-100): "))
    uts = float(input("Masukkan nilai UTS (0-100): "))
    uas = float(input("Masukkan nilai UAS (0-100): "))

    # Menambahkan data ke dalam list
    data_list.append({
        "Nama": nama,
        "NIM": nim,
        "Tugas": tugas,
        "UTS": uts,
        "UAS": uas,
        "Nilai Akhir": hitung_nilai_akhir(tugas, uts, uas)
    })

    # Pertanyaan untuk menambah data lagi
    if input("Apakah ingin menambah data lagi? (y/t): ").lower() == 't':
        break

# Menampilkan daftar data
tampilkan_data(data_list)
