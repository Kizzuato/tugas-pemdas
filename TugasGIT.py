data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500 
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450 
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600 
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550 
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480 
        }
    }
}

# Tampilkan seluruh data dari data_panen termasuk nama lokasi dan hasil panen masing-masing.
for data in data_panen.values():
    print(f"\nNama Lokasi: {data['nama_lokasi']}")
    print("Hasil Panen:")
    for buah, jumlah in data['hasil_panen'].items():
        print(f"- {buah}: {jumlah} kg")
        
# Tampilkan jumlah hasil panen jagung dari lokasi2.
jumlah_jagung = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"\nJumlah Hasil Panen Jagung di Lokasi 2: {jumlah_jagung} kg")

# Tampilkan nama lokasi dari lokasi3.
nama_lokasi = data_panen['lokasi3']['nama_lokasi']
print(f"\nNama Lokasi 3: {nama_lokasi}")

# Masukkan Jumlah Hasil Panen Padi dan Kedelai Setiap Lokasi ke Dalam Variabel yang Berbeda:
padi_lokasi1 = data_panen['lokasi1']['hasil_panen']['padi']
kedelai_lokasi1 = data_panen['lokasi1']['hasil_panen']['kedelai']
padi_lokasi2 = data_panen['lokasi2']['hasil_panen']['padi']
kedelai_lokasi2 = data_panen['lokasi2']['hasil_panen']['kedelai']
padi_lokasi3 = data_panen['lokasi3']['hasil_panen']['padi']
kedelai_lokasi3 = data_panen['lokasi3']['hasil_panen']['kedelai']
padi_lokasi4 = data_panen['lokasi4']['hasil_panen']['padi']
kedelai_lokasi4 = data_panen['lokasi4']['hasil_panen']['kedelai']
padi_lokasi5 = data_panen['lokasi5']['hasil_panen']['padi']
kedelai_lokasi5 = data_panen['lokasi5']['hasil_panen']['kedelai']

print(f"\nJumlah Hasil Panen Padi di Lokasi 1: {padi_lokasi1} kg")
print(f"Jumlah Hasil Panen Kedelai di Lokasi 1: {kedelai_lokasi1} kg")
print(f"\nJumlah Hasil Panen Padi di Lokasi 2: {padi_lokasi2} kg")
print(f"Jumlah Hasil Panen Kedelai di Lokasi 2: {kedelai_lokasi2} kg")
print(f"\nJumlah Hasil Panen Padi di Lokasi 3: {padi_lokasi3} kg")
print(f"Jumlah Hasil Panen Kedelai di Lokasi 3: {kedelai_lokasi3} kg")
print(f"\nJumlah Hasil Panen Padi di Lokasi 4: {padi_lokasi4} kg")
print(f"Jumlah Hasil Panen Kedelai di Lokasi 4: {kedelai_lokasi4} kg")
print(f"\nJumlah Hasil Panen Padi di Lokasi 5: {padi_lokasi5} kg")
print(f"Jumlah Hasil Panen Kedelai di Lokasi 5: {kedelai_lokasi5} kg")