from numpy import mean
import pandas as pd

PATH = "data/processed/contratos_menores_2026_clean.csv"

def kpi_gasto_mes():
    df = pd.read_csv(PATH) 
    
    result = (
    df.groupby("MES", as_index=False)
    .agg({"IMPORTE_ADJUDICACION_IVA_INC": "sum"})
    .sort_values(by="MES")
    )
    
    result.to_csv("data/outputs/kpi_gasto_mes.csv", index=False)
    
    return result


def kpi_contratos_mes():
    df = pd.read_csv(PATH) 
    
    result = (
        df.groupby("MES", as_index=False)
        .agg({"N_DE_REGISTRO_DE_CONTRATO" :"size"})
        .sort_values(by="MES")
    )
    
    result.to_csv("data/outputs/kpi_contratos_mes.csv", index=False)
    
    return result


def kpi_ticket_promedio():
    df = pd.read_csv(PATH) 
    
    result = (
        df.groupby("MES", as_index=False)
        .agg({"IMPORTE_ADJUDICACION_IVA_INC" : 'mean'})
        .sort_values(by="MES")
    )
    
    result.to_csv("data/outputs/kpi_ticket_promedio.csv", index=False)
    
    return result


def kpi_top_empresas_contratos():
    df = pd.read_csv(PATH)
    
    result = (
        df.groupby("RAZON_SOCIAL_ADJUDICATARIO", as_index=False)
        .agg({"N_DE_REGISTRO_DE_CONTRATO" : "size"})
        .sort_values(by= "N_DE_REGISTRO_DE_CONTRATO", ascending=False)
        .rename(columns={"N_DE_REGISTRO_DE_CONTRATO" : "TOTAL_CONTRATOS"})
        .head(10)
    )
    
    result.to_csv("data/outputs/kpi_top_empresas_contratos.csv", index=False)
    
    return result
    
    
def kpi_top_empresas_monto():
    df = pd.read_csv(PATH)
    
    result = (
        df.groupby("RAZON_SOCIAL_ADJUDICATARIO", as_index=False)
        .agg({"IMPORTE_ADJUDICACION_IVA_INC" : "sum"})
        .sort_values(by="IMPORTE_ADJUDICACION_IVA_INC", ascending=False)
        .head(10)
    )
    
    result.to_csv("data/outputs/kpi_top_empresas_monto.csv", index=False)
    
    return result


def kpi_top_organo_contratacion_mes():
    df = pd.read_csv(PATH)
    
    result = (
        df.groupby(["MES", "ORGANO_DE_CONTRATACION"], as_index=False)
        .agg({"IMPORTE_ADJUDICACION_IVA_INC" : "sum"})
        .sort_values(by=["MES", "IMPORTE_ADJUDICACION_IVA_INC"], ascending=[True, False])
        .groupby("MES")
        .head(10)
    )
    
    result.to_csv("data/outputs/kpi_top_organo_contratacion_mes.csv", index=False)
    
    return result 



def kpi_tipo_contrato_mes():
    df = pd.read_csv(PATH)
    
    result = (
        df.groupby(["MES", "TIPO_DE_CONTRATO"], as_index=False)
        .agg({"IMPORTE_ADJUDICACION_IVA_INC" : "sum"})
        .sort_values(by=["MES", "IMPORTE_ADJUDICACION_IVA_INC"], ascending=[True, False])
    )
    
    result.to_csv("data/outputs/kpi_tipo_contrato_mes.csv", index=False)
    
    return result
