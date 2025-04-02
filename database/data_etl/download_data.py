from pathlib import Path
import requests
from requests.exceptions import RequestException

from config import (
    DEMONSTRACOES_DIR,
    OPERADORAS_DIR,
    OPERADORAS_CSV_URL, 
    URLS_ZIP,
    )

def download_files(url:str, path: Path):
    try:
        response = requests.get(url,stream=True,timeout=10)
        response.raise_for_status()

        with open(path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
    
    except RequestException as e:
        print(f"Erro ao fazer o download do arquivo: {e}")

def download_demonstracoes_contabeis():
    for arquivo,url in URLS_ZIP.items():
        path = DEMONSTRACOES_DIR/f"{arquivo}.zip"
        download_files(url,path)

def download_operadoras_csv():
    path = OPERADORAS_DIR/"operadoras_ativas.csv"
    download_files(OPERADORAS_CSV_URL,path)



