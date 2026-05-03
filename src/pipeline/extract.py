import pandas as pd
from pathlib import Path

def load_data(path):
    ext = Path(path).suffix.lower()
    
    if ext == ".csv":
        return pd.read_csv(path, sep=";", encoding="latin-1")
    
    if ext in [".xlsx", "xls"]:
        return pd.read_excel(path)
    
    raise ValueError(f"Formato no soportado: {ext}")