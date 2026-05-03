
from pandas import DataFrame
import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns
        .str.strip()
        .str.upper()
        .str.replace(" - ", "_", regex=False) 
        .str.replace(" ", "_")                    
        .str.replace(".", "", regex=False) 
        .str.replace(r"[^\w]", "", regex=True)
    )
    return df

def clean_string_columns(df: pd.DataFrame) -> pd.DataFrame: # type: ignore
    columns = [
        'RAZON_SOCIAL_ADJUDICATARIO',
        'TIPO_DE_CONTRATO',
        'ORGANO_DE_CONTRATACION',
        'ORGANISMO_CONTRATANTE',
        'ORGANISMO_PROMOTOR',
        'PYME',
        'CENTRO_SECCION'
    ]
    
    for col in columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.upper()
            .str.strip()
            .str.replace(r'\s+', ' ', regex=True)
        )
    return df


def clean_decimal_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    
    for col in columns:
        clean_series = (
            df[col]
            .astype(str)
            .str.replace(r'[^\d,.-]', '', regex=True) 
            .str.replace('.', '', regex=False)         
            .str.replace(',', '.', regex=False) 
        )
        df[col] = pd.to_numeric(clean_series, errors='coerce')
        df[col] = df[col].fillna(0.0).astype(float)
    
    return df


def clean_money_columns(df: pd.DataFrame) -> pd.DataFrame:
    money_columns = df.filter(like='IMPORTE').columns.tolist()
    return clean_decimal_columns(df, money_columns)


def clean_plazo_column(df: pd.DataFrame) -> pd.DataFrame:
    return clean_decimal_columns(df, ['PLAZO'])

    
def clean_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    columns = [
        'N_DE_INVITACIONES_CURSADAS',
        'N_LICITADORES_PARTICIPANTES'
    ] 
    
    df[columns] = (
        df[columns]
        .apply(pd.to_numeric, errors='coerce')
        .fillna(0)
        .astype(int)
    )
    
    return df
    

def clean_date_columns(df: pd.DataFrame) -> pd.DataFrame:
    date_columns = ["FECHA_DE_ADJUDICACION", "FECHA_DE_INSCRIPCION"] 
    
    for col in date_columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .replace({"": None, "nan": None})
        )
        
        df[col] = pd.to_datetime(
        df[col],
        format="%d/%m/%y",
        errors="coerce"
        )
        
    return df  


def create_time_columns(df: pd.DataFrame) -> pd.DataFrame:
    df['MES'] = df['FECHA_DE_ADJUDICACION'].dt.strftime('%Y-%m')
    return df

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = clean_column_names(df)
    df = clean_string_columns(df)
    df = clean_money_columns(df)
    df = clean_plazo_column(df)
    df = clean_numeric_columns(df)
    df = clean_date_columns(df)
    df = create_time_columns(df)
    
    return df

        