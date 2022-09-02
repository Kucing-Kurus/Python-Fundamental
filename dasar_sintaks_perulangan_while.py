'''
program perulangan dengan while
'''
import os
os.system("cls")
print("="*10,"perulangan While","="*10)

jumlah_buku = 10
jumlah_buku_yang_sudah_dibaca = 0
print('Ibu perintahkan,"Baca semua bukumu"')
print(f"Jumlah buku yang sudah dibaca = {jumlah_buku_yang_sudah_dibaca}\n")

while jumlah_buku_yang_sudah_dibaca < jumlah_buku:
    jumlah_buku_yang_sudah_dibaca = jumlah_buku_yang_sudah_dibaca + 1
    print(f"Buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca")

print(f"Jumlah buku yang sudah dibaca = {jumlah_buku_yang_sudah_dibaca}")