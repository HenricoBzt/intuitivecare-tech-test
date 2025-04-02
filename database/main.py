from config import (
    DEMONSTRACOES_DIR,
    EXTRACTED_DIR,
    CSV_PROCESSED_DIR
)

from data_etl.download_data import (
    download_demonstracoes_contabeis,
    download_operadoras_csv,
)

from data_etl.extract import extract_zip
from data_etl.transform import convert_csv_encoding

if __name__ == "__main__":
    print("Iniciando o download dos demonstrativos contábeis...")
    download_demonstracoes_contabeis()

    print("Iniciando o download das operadoras...")
    download_operadoras_csv()
    print("Download finalizado!\n")

    print("Iniciando a extração dos arquivos...")
    extract_zip(DEMONSTRACOES_DIR, EXTRACTED_DIR)
    print("Extração finalizada!\n")

    print("Iniciando a conversão dos arquivos...")
    convert_csv_encoding(EXTRACTED_DIR, CSV_PROCESSED_DIR)
    print("Conversão finalizada!")