
from pathlib import Path
import requests
import zipfile

BASEDIR = Path(__file__).parent
PDF_FILES = Path(BASEDIR/'pdf_files')
PDF_FILES.mkdir(exist_ok=True)

ZIP_FILES = Path(BASEDIR/'zip_files')
ZIP_FILES.mkdir(exist_ok=True)

def download_pdf(url: str, filename:str):

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        path_save = PDF_FILES / filename
        with open(path_save, 'wb') as fn:
            for chunck in response.iter_content(chunk_size=8192):
                fn.write(chunck)

        if path_save.exists():
            print(f"PDF BAIXADO: {filename}")
            return path_save
        
        else:
            print(f"Erro ao baixar o PDF: {filename}")
            return None


    except requests.exceptions.RequestException as e:
        print("Erro ao fazer a requisição: {e}")



def to_zip(files_pdf_path: list, zip_name: str = 'ANS_PDF.zip'):
    try:
        
        zip_pach = ZIP_FILES / zip_name

        with zipfile.ZipFile(zip_pach,'w') as zipf:
            for pdf in files_pdf_path:
                if Path(pdf).exists():
                    zipf.write(pdf, arcname=Path(pdf).name)

        print(f"Arquivo {zip_name} adicionado ao arquivo zip.")
        
   
    except Exception as e:
        print(f"Erro ao criar ZIP: {e}")    
        


