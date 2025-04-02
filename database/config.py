from pathlib import Path

# URL PARA DONWLOAD DE DADOS ZIP DE DESEMONSTRATIVOS CONTÁBEIS
URLS_ZIP = {
    "1T2023": "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2023/1T2023.zip",
    "2T2023": "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2023/2T2023.zip",
    "3T2023": "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2023/3T2023.zip",
    "4T2023": "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2023/4T2023.zip",
    "1T2024": "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2024/1T2024.zip",
    "2T2024": "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2024/2T2024.zip",
    "3T2024": "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2024/3T2024.zip",
    "4T2024": "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2024/4T2024.zip",
}

# URL PARA DOWNLOAD DE DADOS DE OPERADORAS
OPERADORAS_CSV_URL = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv"


PROJECT_ROOT = Path(__file__).resolve().parent.parent 

# Diretórios de dados
DATA_DIR = PROJECT_ROOT / "database" / "data_zips"
DEMONSTRACOES_DIR = DATA_DIR / "demonstracoes_contabeis"
OPERADORAS_DIR = DATA_DIR / "operadoras"

# Diretórios de extração e processamento
EXTRACTED_DIR = PROJECT_ROOT / "database" / "data_etl" / "extract"
CSV_PROCESSED_DIR = PROJECT_ROOT / "database" / "data_etl" / "csv_processed"

# Criar diretórios se não existirem
DATA_DIR.mkdir(parents=True, exist_ok=True)
DEMONSTRACOES_DIR.mkdir(parents=True, exist_ok=True)

OPERADORAS_DIR.mkdir(parents=True, exist_ok=True)

EXTRACTED_DIR.mkdir(parents=True, exist_ok=True)
CSV_PROCESSED_DIR.mkdir(parents=True, exist_ok=True)