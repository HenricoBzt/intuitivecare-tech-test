import pdfplumber
import pandas as pd
from pathlib import Path
import zipfile


# Função para normalizar as tabelas caso vierem incosistentes
def normalize_table(table: list,expected_columns:int):

    if not table:
        return None
    
    headers = table[0]
    if len(headers) < expected_columns:
        headers += ['col'] * (expected_columns - len(headers))

    elif len(headers) > expected_columns:
        headers = headers[:expected_columns]
    
    new_headers = []
    for i, header in enumerate(headers):
        if header in new_headers: 
            new_header = f"{header}_{i}"
        else:
            new_header = header
        new_headers.append(new_header)

    normalized_data = []

    for row in table[1:]:
        if len(row) < expected_columns:
            row += [''] * (expected_columns - len(row))
            
        elif len(row) > expected_columns:
            row = row[:expected_columns]
        normalized_data.append(row)

    return [new_headers] + normalized_data

# Extrair tabelas do PDF
def extract_tables_pdf(pdf_path: Path, expected_columns: int):
    dfs = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()

                if not tables:
                    continue    
                
                for table in tables:
                    # Normaliza a tabela
                    if normalized_table := normalize_table(table, expected_columns):
                        dfs.append(
                            pd.DataFrame(normalized_table[1:], columns=normalized_table[0])
                            )
                        
        return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()
    
    except Exception as e:
        print(f"Erro ao extrair tabelas do PDF: {e}")
        return None
    
def rename_columns(df: pd.DataFrame):
    columns_mapping ={
        "OD": "Odontológica",
        "AMB": "Ambulatorial"
    }
    return df.rename(columns=columns_mapping)
    
# Salvar tabelas em CSV
def save_csv(df: pd.DataFrame, path: Path):

    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(path,index=False,encoding='utf-8-sig')
        print(f"CSV salvo: {path}")
    
    except Exception as e:
        print(f"Erro ao salvar o CSV: {e}")


def csv_compact_zip(csv_path: Path, zip_dir: Path ,zip_name: str = "Teste_Henrico.zip"):

    try:
        zip_dir.mkdir(parents=True,exist_ok=True)
        zip_path  = zip_dir/zip_name

        with zipfile.ZipFile(zip_path, 'w') as zipf:
            zipf.write(csv_path, arcname=csv_path.name)
            print(f"Arquivo {zip_name} adicionado com sucesso em {zip_path}")
    
    except Exception as e:
        print(f"Ocorreu um erro ao compactar o csv {e}")






                        



