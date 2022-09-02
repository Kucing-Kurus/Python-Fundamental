'''
program perulangan for
'''
import os
os.system("cls")

## Perulangan
print("="*10,"Perulangan for","="*10)

jumlah_buku = 10
jumlah_buku_yang_sudah_dibaca = 0
print('Ibu perintahkan,"Baca semua bukumu"')
print(f"Jumlah buku = {jumlah_buku}\n")

for jumlah_buku_yang_sudah_dibaca in range(1,jumlah_buku+1):
    print(f"Buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca")

print(f"Jumlah buku yang sudah dibaca = {jumlah_buku_yang_sudah_dibaca}")