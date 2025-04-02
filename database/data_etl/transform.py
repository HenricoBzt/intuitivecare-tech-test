import pandas as pd
from pathlib import Path

def convert_csv_encoding(input_dir: Path, output_dir: Path):

    output_dir.mkdir(parents=True, exist_ok=True)
    
    for csv_file in input_dir.glob("*.csv"):
        try:
             df = pd.read_csv(
                csv_file,
                delimiter=';',
                encoding='utf-8',  
                dtype={"REG_ANS": str},
                decimal=',',
                thousands='.',
                parse_dates=['DATA'],  
                dayfirst=True  
            )
             
             df['DATA'] = df['DATA'].dt.strftime('%d/%m/%Y')

             output_file = output_dir / csv_file.name
             df.to_csv(
                    output_file, 
                    sep=';',
                    index=False, 
                    encoding='utf-8',
                    date_format='%Y-%m-%d'
                )
             print(f"Arquivo Tratado: {csv_file.name}")

             
        except Exception as e:
            print(f"Erro em {csv_file.name}: {str(e)}")
