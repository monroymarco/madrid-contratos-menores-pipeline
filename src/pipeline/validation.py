import pandas as pd
import logging

def validate_contract_id(df: pd.DataFrame) -> None:
    col = 'N_DE_REGISTRO_DE_CONTRATO'
    
    nulls = df[col].isna().sum()
    dups = df[col].duplicated().sum()
    
    if nulls > 0:
        logging.warning(f'{nulls} nulos en {col}')
    if dups > 0:
       logging.warning(f'{dups} duplicados en {col}')
    if nulls == 0 and dups == 0:
        logging.info(f' {col} OK: sin nulos ni duplicados')
        
        
