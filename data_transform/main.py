from tables_pdf import extract_tables_pdf, save_csv,csv_compact_zip,rename_columns
from pathlib import Path




if __name__ == "__main__":
    BASE_DIR = Path(__file__).parent
    CSV_DIR = Path(BASE_DIR/"csv_files")
    PDF_DIR = Path(BASE_DIR/"pdf")
    ZIP_DIR= Path(BASE_DIR/"zip_files")
    
    PDF_DIR.mkdir(parents=True, exist_ok=True)

    CSV_PATH = Path(CSV_DIR/"Anexo_I_Rol_2021RN_465.2021_RN627L.2024.csv")
    PDF_PATH = Path(PDF_DIR/"Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf")
    ZIP_NAME = "Teste_Henrico.zip"
    EXPECTED_COLUMNS = 13
    
    df = extract_tables_pdf(PDF_PATH, EXPECTED_COLUMNS)
    
    if df is not None and not df.empty:
        df = rename_columns(df)
        save_csv(df, CSV_PATH)
        csv_compact_zip(CSV_PATH,ZIP_DIR, ZIP_NAME)
        
    else:
        print("⚠️ Nenhum dado foi processado. Verifique o PDF de entrada.")

