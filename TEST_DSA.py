# Import dataset
import pandas as pd
import numpy as np

dataset_lokasi = pd.read_csv('catatan_lokasi.csv')
dataset_profil = pd.read_csv('data_profil.csv')
dataset_id = dataset_profil.merge(dataset_lokasi, on = 'id', how = 'inner')

# Kemungkinan pertanyaan
''' Pada tanggal berapa (salah satu divisi disebut) sering berada di suatu tempat tertentu?'''
print('Pada tanggal berapa (salah satu divisi disebut) sering berada di suatu tempat tertentu?')
# Coding
tempat = dataset_id.groupby('lokasi_dominan')
while True:
    dimana = str(input('Masukan tempat: '))
    data_tempat = tempat.get_group(dimana)
    print(data_tempat.groupby('divisi').size())
    lanjut = str(input('lanjut Y/N: '))
    if lanjut == 'n':
        break