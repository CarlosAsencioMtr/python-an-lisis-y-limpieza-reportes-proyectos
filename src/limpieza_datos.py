import pandas as pd


def cargar_datos(ruta_archivo):
    df = pd.read_csv(ruta_archivo)
    return df


def limpiar_datos(df):
    df.columns = df.columns.str.strip().str.lower()

    columnas_texto = [
        "codigo_proyecto",
        "nombre_proyecto",
        "direccion",
        "responsable",
        "estado"
    ]

    for columna in columnas_texto:
        df[columna] = df[columna].astype(str).str.strip()

    # Convertir columnas de fecha
    columnas_fecha = [
        "fecha_inicio",
        "fecha_fin_estimada",
        "fecha_fin_real",
        "ultima_actualizacion"
    ]

    for columna in columnas_fecha:
        df[columna] = pd.to_datetime(df[columna], errors="coerce")

    # Convertir valores numéricos
    df["porcentaje_avance"] = pd.to_numeric(df["porcentaje_avance"], errors="coerce")
    df["presupuesto"] = pd.to_numeric(df["presupuesto"], errors="coerce")

    # Estandarizar estado
    df["estado"] = df["estado"].str.title()

    return df


def validar_datos(df):
 

    validaciones = {
        "total_registros": len(df),
        "valores_nulos_por_columna": df.isnull().sum().to_dict(),
        "proyectos_duplicados": df["codigo_proyecto"].duplicated().sum(),
        "avance_mayor_100": len(df[df["porcentaje_avance"] > 100]),
        "avance_menor_0": len(df[df["porcentaje_avance"] < 0]),
        "proyectos_sin_responsable": len(df[df["responsable"].isnull()])
    }

    return validaciones


if __name__ == "__main__":
    ruta = "data/proyectos_ejemplo.csv"

    datos = cargar_datos(ruta)
    datos_limpios = limpiar_datos(datos)
    resumen_validacion = validar_datos(datos_limpios)

    print("Datos cargados y limpiados correctamente.")
    print(resumen_validacion)
