from tables_pdf import extract_tables_pdf, save_csv,csv_compact_zip,rename_columns
from pathlib import Path




if __name__ == "__main__":
    BASE_DIR = Path(__file__).parent
    PDF_PATH = Path(BASE_DIR/"pdf_files/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf")
    CSV_PATH = Path(BASE_DIR/"csv_files/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.csv")
    ZIP_PATH = Path(BASE_DIR/"zip_files")
    EXPECTED_COLUMNS = 13
    df = extract_tables_pdf(PDF_PATH, EXPECTED_COLUMNS)
    
    if df is not None and not df.empty:
        df = rename_columns(df)
        save_csv(df, CSV_PATH)
        csv_compact_zip(CSV_PATH,ZIP_PATH,"Teste_Henrico.zip")
        
    else:
        print("⚠️ Nenhum dado foi processado. Verifique o PDF de entrada.")

