from zipfile import ZipFile
from pathlib import Path


def extract_zip(zip_path: Path, extract_dir: Path):
    try:
        for zip_file in zip_path.glob("*.zip"):
            with ZipFile(zip_file, 'r') as zipf:
                zipf.extractall(extract_dir)
                print(f"Arquivo extraído: {zip_file.name}")
    
    except Exception as e:
        print(f"Erro ao extrair o arquivo {zip_path.name}: {e}")