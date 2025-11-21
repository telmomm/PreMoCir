import wfdb 
import requests
from bs4 import BeautifulSoup
import re
import os
import pandas as pd

# Create ECG Cardiac Surgery Dataset
cardiac_surgery_df = pd.read_csv('aux_dataset/30dm_cardiac_surgery_dataset.csv')
ecg_index_df = pd.read_csv('MIMIC-IV/ECG/record_list.csv')

#Crear un nuevo df que sea ecg_index:df, pero unicamente los subject_id que coincidan con los de cardiac_surgery_df y si hay varios reghistros subject_id con el mismo npmbre, cpger el que en ecg_time sea más nuevo

ecg_cardiac_surgery_df = ecg_index_df[ecg_index_df['subject_id'].isin(cardiac_surgery_df['subject_id'])]
ecg_cardiac_surgery_df = ecg_cardiac_surgery_df.loc[ecg_cardiac_surgery_df.groupby('subject_id')['ecg_time'].idxmax()]
#Añade tambien de cardiac_surgery los procedures, el prodecure date el deathtime y el mortality_30d

ecg_cardiac_surgery_df = ecg_cardiac_surgery_df.merge(cardiac_surgery_df[['subject_id', 'procedures', 'procedure_date', 'deathtime', 'mortality_30d']], on='subject_id', how='left')

ecg_cardiac_surgery_df.to_csv('aux_dataset/ecg_cardiac_surgery_dataset.csv', index=False)
print("Dataset de ECG de pacientes de cirugía cardíaca guardado en aux_dataset/ecg_cardiac_surgery_dataset.csv")


# Download ECG Records
import csv

download_status = set()
log_file = 'LOGS/ecg_downloading_log.csv'

# Inicializa el archivo de log si no existe
if not os.path.exists(log_file):
    with open(log_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'filename', 'extension', 'status', 'http_code', 'error'])

for id in range(ecg_cardiac_surgery_df.shape[0]):
    storage_path = f'/Volumes/KINGSTON/MIMIC-IV/ECG/{ecg_cardiac_surgery_df.iloc[id]["path"]}'
    storage_path = storage_path[:storage_path.rfind('/')]
    download_path = f'https://physionet.org/files/mimic-iv-ecg/1.0/{ecg_cardiac_surgery_df.iloc[id]["path"]}'
    filename = ecg_cardiac_surgery_df.iloc[id]["path"]

    if not os.path.exists(storage_path):
        os.makedirs(storage_path, exist_ok=True)
        print(f"Descargando {storage_path}...")

    file_extension = [".dat", ".hea"]
    for ext in file_extension:
        download_url = f'{download_path}{ext}?download'
        print(f"Desde {download_url}...")
        status = 'error'
        http_code = ''
        error_msg = ''
        try:
            response = requests.get(download_url, timeout=30)
            http_code = response.status_code
            local_file = f'/Volumes/KINGSTON/MIMIC-IV/ECG/{ecg_cardiac_surgery_df.iloc[id]["path"]}{ext}'
            if response.status_code == 200:
                with open(local_file, 'wb') as f:
                    f.write(response.content)
                status = 'descargado'
            else:
                error_msg = f'HTTP {response.status_code}'
                print(f"Error al descargar {local_file}: {response.status_code}")
        except Exception as e:
            error_msg = str(e)
            print(f"Excepción al descargar {local_file}: {e}")
        # Registrar en el log
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([id, filename, ext, status, http_code, error_msg])