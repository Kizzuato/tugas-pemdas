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
padi = {}
kedelai = {}

for key, lokasi in data_panen.items():
    padi[key] = lokasi['hasil_panen']['padi']
    kedelai[key] = lokasi['hasil_panen']['kedelai']

print("Data Padi:", padi)
print("Data Kedelai:", kedelai)

# Buat Percabangan
for data in data_panen.values():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    nama = data['nama_lokasi']

    if padi > 1300 or jagung > 800:
        print(f"{nama} : Perlu perhatian khusus")
    else:
        print(f"{nama} : Kondisi baik")

print("Program Selesai !")
