import logging

from pipeline.validation import validate_contract_id
from pipeline.extract import load_data
from pipeline.transform import transform
from pipeline.load import save_data

from pipeline.kpis import (
    kpi_gasto_mes,
    kpi_contratos_mes,
    kpi_ticket_promedio,
    kpi_top_empresas_contratos,
    kpi_top_empresas_monto,
    kpi_top_organo_contratacion_mes,
    kpi_tipo_contrato_mes
)

RAW_PATH = "data/raw/contratos_menores_2026.xlsx"
CLEAN_PATH = "data/processed/contratos_menores_2026_clean.csv"

logging.basicConfig(level=logging.INFO)


def run_kpis():
    kpi_gasto_mes()
    kpi_contratos_mes()
    kpi_ticket_promedio()
    kpi_top_empresas_contratos()
    kpi_top_empresas_monto()
    kpi_top_organo_contratacion_mes()
    kpi_tipo_contrato_mes()


def main():
    df = load_data(RAW_PATH)
    df = transform(df)
    validate_contract_id(df)
    save_data(df, CLEAN_PATH)
    
    run_kpis()
    
    
if __name__ == "__main__":
    main()
    


