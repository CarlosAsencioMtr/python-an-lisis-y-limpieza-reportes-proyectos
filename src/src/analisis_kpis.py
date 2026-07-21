import pandas as pd


def calcular_kpis(df):
    """
    Calcula indicadores principales para monitoreo de proyectos.
    """

    total_proyectos = len(df)
    proyectos_activos = len(df[df["estado"] == "Activo"])
    proyectos_finalizados = len(df[df["estado"] == "Finalizado"])
    proyectos_nuevos = len(df[df["estado"] == "Nuevo"])
    proyectos_atrasados = len(df[df["estado"] == "Atrasado"])

    avance_promedio = round(df["porcentaje_avance"].mean(), 2)
    presupuesto_total = round(df["presupuesto"].sum(), 2)

    kpis = {
        "total_proyectos": total_proyectos,
        "proyectos_activos": proyectos_activos,
        "proyectos_finalizados": proyectos_finalizados,
        "proyectos_nuevos": proyectos_nuevos,
        "proyectos_atrasados": proyectos_atrasados,
        "avance_promedio": avance_promedio,
        "presupuesto_total": presupuesto_total
    }

    return kpis


def proyectos_por_estado(df):
    """
    Agrupa proyectos por estado.
    """
    return df.groupby("estado").size().reset_index(name="total_proyectos")


def avance_por_direccion(df):
    """
    Calcula avance promedio por dirección.
    """
    return (
        df.groupby("direccion")["porcentaje_avance"]
        .mean()
        .round(2)
        .reset_index(name="avance_promedio")
        .sort_values(by="avance_promedio", ascending=False)
    )


def proyectos_por_responsable(df):
    """
    Calcula cantidad de proyectos por responsable.
    """
    return (
        df.groupby("responsable")
        .size()
        .reset_index(name="total_proyectos")
        .sort_values(by="total_proyectos", ascending=False)
    )


def identificar_proyectos_atrasados(df):
    """
    Identifica proyectos atrasados según estado o fecha estimada vencida.
    """

    fecha_referencia = pd.to_datetime("2026-07-21")

    atrasados = df[
        (df["estado"] == "Atrasado") |
        ((df["fecha_fin_estimada"] < fecha_referencia) & (df["estado"] != "Finalizado"))
    ]

    return atrasados


if __name__ == "__main__":
    from limpieza_datos import cargar_datos, limpiar_datos

    ruta = "data/proyectos_ejemplo.csv"

    datos = cargar_datos(ruta)
    datos_limpios = limpiar_datos(datos)

    print("KPIs principales:")
    print(calcular_kpis(datos_limpios))

    print("\nProyectos por estado:")
    print(proyectos_por_estado(datos_limpios))

    print("\nAvance por dirección:")
    print(avance_por_direccion(datos_limpios))

    print("\nProyectos atrasados:")
    print(identificar_proyectos_atrasados(datos_limpios))
