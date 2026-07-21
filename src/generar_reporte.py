import os
import pandas as pd
import matplotlib.pyplot as plt

from limpieza_datos import cargar_datos, limpiar_datos
from analisis_kpis import (
    calcular_kpis,
    proyectos_por_estado,
    avance_por_direccion,
    proyectos_por_responsable,
    identificar_proyectos_atrasados
)


def crear_carpetas_salida():
    """
    Crea carpetas de salida si no existen.
    """

    os.makedirs("outputs", exist_ok=True)
    os.makedirs("outputs/graficos", exist_ok=True)


def generar_grafico_proyectos_por_estado(df_estado):
    """
    Genera gráfico de proyectos por estado.
    """

    plt.figure()
    plt.bar(df_estado["estado"], df_estado["total_proyectos"])
    plt.title("Proyectos por Estado")
    plt.xlabel("Estado")
    plt.ylabel("Total de Proyectos")
    plt.tight_layout()
    plt.savefig("outputs/graficos/proyectos_por_estado.png")
    plt.close()


def generar_grafico_avance_por_direccion(df_avance):
    """
    Genera gráfico de avance promedio por dirección.
    """

    plt.figure()
    plt.bar(df_avance["direccion"], df_avance["avance_promedio"])
    plt.title("Avance Promedio por Dirección")
    plt.xlabel("Dirección")
    plt.ylabel("Avance Promedio (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/graficos/avance_por_direccion.png")
    plt.close()


def generar_reporte_excel(df, kpis, df_estado, df_avance, df_responsable, df_atrasados):
    """
    Genera un archivo Excel con los resultados del análisis.
    """

    resumen_kpis = pd.DataFrame([kpis])

    with pd.ExcelWriter("outputs/reporte_proyectos.xlsx", engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="datos_limpios", index=False)
        resumen_kpis.to_excel(writer, sheet_name="kpis", index=False)
        df_estado.to_excel(writer, sheet_name="proyectos_estado", index=False)
        df_avance.to_excel(writer, sheet_name="avance_direccion", index=False)
        df_responsable.to_excel(writer, sheet_name="proyectos_responsable", index=False)
        df_atrasados.to_excel(writer, sheet_name="proyectos_atrasados", index=False)

    resumen_kpis.to_csv("outputs/resumen_kpis.csv", index=False)


def ejecutar_reporte():
    """
    Ejecuta el flujo completo del análisis.
    """

    crear_carpetas_salida()

    ruta = "data/proyectos_ejemplo.csv"

    datos = cargar_datos(ruta)
    datos_limpios = limpiar_datos(datos)

    kpis = calcular_kpis(datos_limpios)
    df_estado = proyectos_por_estado(datos_limpios)
    df_avance = avance_por_direccion(datos_limpios)
    df_responsable = proyectos_por_responsable(datos_limpios)
    df_atrasados = identificar_proyectos_atrasados(datos_limpios)

    generar_grafico_proyectos_por_estado(df_estado)
    generar_grafico_avance_por_direccion(df_avance)

    generar_reporte_excel(
        datos_limpios,
        kpis,
        df_estado,
        df_avance,
        df_responsable,
        df_atrasados
    )

    print("Reporte generado correctamente.")
    print("Archivos creados en la carpeta outputs.")


if __name__ == "__main__":
    ejecutar_reporte()
