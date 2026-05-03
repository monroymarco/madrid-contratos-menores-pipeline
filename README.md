# Data Pipeline - Contratos Madrid

Pipeline ETL en Python que procesa datos de contratos menores del Ayuntamiento de Madrid (CSV/XLSX), realiza limpieza, validación y genera KPIs.

---

## Arquitectura

raw → processed → outputs

---

## Flujo

1. Extract → lectura de CSV/XLSX
2. Transform → limpieza (columnas, texto, fechas, importes)
3. Validation → control de nulos y duplicados
4. Load → guardado en processed
5. KPIs → generación de métricas

---

## Estructura

data/
raw/ → datos originales (csv/xlsx)
processed/ → datos limpios
outputs/ → KPIs generados

notebooks/
01_exploracion.ipynb
02_analisis.ipynb

src/pipeline/
extract.py
transform.py
load.py
validation.py
kpis.py
main.py

---

## KPIs

- Gasto por mes
- Contratos por mes
- Ticket promedio
- Top empresas (monto y contratos)
- Tipo de contrato por mes

## Tecnologías

- Python
- pandas

---

## Ejecución

```bash
PYTHONPATH=src python3 -m pipeline.main
```

## Autor

Marco Monroy<br>  
Data Engineering | Python | SQL
