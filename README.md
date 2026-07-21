# Python para Análisis y Automatización de Reportes de Proyectos

Este proyecto utiliza Python para limpiar, validar, analizar y generar reportes a partir de datos ficticios de proyectos.

El objetivo es demostrar cómo Python puede apoyar procesos de análisis de datos, automatización de reportes y generación de indicadores para monitoreo empresarial.

## Objetivo

Automatizar el análisis de reportes de proyectos mediante Python, calculando KPIs, generando gráficos y exportando resultados para facilitar la toma de decisiones.

## Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- OpenPyXL
- CSV
- Excel

## Funcionalidades principales

- Carga de datos desde archivo CSV.
- Limpieza y transformación de datos.
- Validación básica de calidad de datos.
- Cálculo de indicadores clave.
- Identificación de proyectos atrasados.
- Análisis por estado, dirección y responsable.
- Generación de gráficos.
- Exportación de reportes a Excel y CSV.

## KPIs calculados

- Total de proyectos
- Proyectos activos
- Proyectos finalizados
- Proyectos nuevos
- Proyectos atrasados
- Avance promedio general
- Presupuesto total
- Proyectos por estado
- Avance promedio por dirección
- Proyectos por responsable

## Estructura del repositorio

```text
python-analisis-reportes-proyectos/
├── README.md
├── requirements.txt
├── data/
│   ├── README.md
│   └── proyectos_ejemplo.csv
├── notebooks/
│   └── README.md
├── src/
│   ├── limpieza_datos.py
│   ├── analisis_kpis.py
│   └── generar_reporte.py
├── outputs/
│   ├── README.md
│   └── graficos/
│       └── README.md
└── docs/
    ├── objetivo-proyecto.md
    ├── diccionario-datos.md
    └── metodologia.md
