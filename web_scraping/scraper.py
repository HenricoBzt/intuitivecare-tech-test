import requests
from bs4 import BeautifulSoup

def find_page(url: str, headers:dict):
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        return response
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
        return None
    


def extract_links_pdf(soup: BeautifulSoup):
    getlink = soup.find_all("a", class_='internal-link', href=True)
    target_links = []

    for link in getlink:
        text = link.text
        href_pdf = link['href']

        if ("Anexo I" in text or "Anexo II" in text) and (href_pdf.endswith('.pdf')):
             target_links.append(href_pdf)

    if not target_links:
        print("Não foram encontrados links para ambos os anexos")
        
    
    if len(target_links) < 2:
        print("Não foram encontrados links para ambos os anexos")  
                  
    return target_links                             