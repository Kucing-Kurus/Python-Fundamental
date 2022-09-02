'''
program perulangan dengan while (unfind)
'''
import os
os.system("cls")
print("="*10,"perulangan While unfind","="*10)

jumlah_buku = 10
jumlah_buku_yang_sudah_dipahamu = 0
jumlah_baca = 0

print('Ibu perintahkan,"Baca semua bukumu sampai paham"')
print(f"Jumlah buku yang sudah dibaca dan dipahami= {jumlah_buku_yang_sudah_dipahamu}\n")

while jumlah_baca < jumlah_buku * 2:
    jumlah_baca = jumlah_baca + 1
    if jumlah_buku_yang_sudah_dipahamu == 7:
        print(f"Buku ke {jumlah_buku_yang_sudah_dipahamu + 1} belum paham")
    else:
        jumlah_buku_yang_sudah_dipahamu = jumlah_buku_yang_sudah_dipahamu + 1
        print(f"Buku ke {jumlah_buku_yang_sudah_dipahamu} sudah dibaca dan dipahami")

print(f"Jumlah buku yang sudah dibaca dan dipahami = {jumlah_buku_yang_sudah_dipahamu}")
if jumlah_buku_yang_sudah_dipahamu == jumlah_buku:
    print(f"Bu, semua buku sudah dibaca dan dipahami")
else:
    print(F"Bu, tidak semua buku bisa dipahami, Budi hanya bisa mehamabi {jumlah_buku_yang_sudah_dipahamu} buku")