'''
semua sintaksis dasar bahasa pemrogaman terdiri dari :
1. Sekuensional : langkah berurutan
2. Percabangan : langkah melompat jika kondisi mempenuhi
3. Perulangan : mengulang langkah berkali kali selama / sampai kondisi terpenuhi
'''
import os
os.system("cls")

## Sekuensial
print("="*20,"Sekuensional","="*20)
print('Ibu berkata,"Pergi ke toko"')
print('Budi menjawab,"Baik, apa yang harus saya lakukan di tokok ?"')
print('Ibu menjawab,"Beli 1 botol susu, dan jika ada telur beli 6"')
print("Maka Budi berangkat ke toko")
print("Dan mulai berbelanja")

## Percabangan
print("="*20,"Percabangan","="*20)
jumlah_botol_susu = 150
jumlah_telur = 1500
print(f"Jumlah botol susu  = {jumlah_botol_susu}")
print(f"Jumlah telur  = {jumlah_telur}\n")

if jumlah_botol_susu > 0:
    print(f"Budi mengecek harga, dan ternyata uangnya cukup")
    if jumlah_telur == 0:
        print(f"Budi membeli 1 botol susu")
    else:
        print(f"Budi membeli 6 botol susu")
else:
    print(f"Budi tidak jadi membeli 1 botol susu")

print(f"Budi pulang kerumah")
print(f"Menyampaikannya kepada ibu")

## Perulangan
print("="*20,"Perulangan","="*20)


