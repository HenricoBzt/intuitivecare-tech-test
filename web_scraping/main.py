import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from scraper import buscar_pagina, extrair_links_pdf
from download_and_zip import download_pdf, to_zip

load_dotenv()

URL = os.getenv('ANS_URL')
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def main():
        
        if URL is None:
            print(" A variável do ambiente 'ANS_URL' não está definida.")
            return 
        
        response = buscar_pagina(URL, HEADERS)
        if response is None:
            print("Falha ao carregar a página.")

        soup = BeautifulSoup(response.text, 'html.parser')
        target_links = extrair_links_pdf(soup)
        print(f'Links de pdf encontrados!\n ANEXO 1: {target_links[0]}\n ANEXO 2: {target_links[1]}')

        files_downloads = []

        for link in target_links:
            filename = link.split('/')[-1]
            file_path = download_pdf(link, filename)
            
            if file_path:
                files_downloads.append(file_path)

        if files_downloads:
            to_zip(files_downloads)
            


if __name__ == "__main__":
     main()
