usia = int(input("masukkan usia pengunjung:"))
hari = input("Apakah hari ini hari libur?".lower()

if hari == "libur" :
    if usia < 12:
        harga = 35000
    elif 12 <= usia <= 64:
        harga = 60000
    else:
        harga = 45000
else :
    hari == "reguler" 
    if usia < 12:
        harga = 30000
    elif 12 <= usia <= 64:
        harga = 50000
    else:
        harga = 40000
    


print(f"Harga tiket: Rp{harga}")

total_detik = int(input("Masukkan jumlah detik: "))

jam = total_detik // 3600
sisa_detik = total_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print(f"{jam}:{menit}:{detik}")
