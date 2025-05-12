"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    import os
    import pandas as pd

    def convertir_fecha(fecha):
        value = pd.to_datetime(fecha, format="%d/%m/%Y", errors="coerce")
        if pd.isna(value):
            value = pd.to_datetime(fecha, format="%Y/%m/%d", errors="coerce")
        return value

    output_dir = "files/output/"
    output_file = "solicitudes_de_credito.csv"

    os.makedirs(output_dir, exist_ok=True)

    df = pd.read_csv("files/input/solicitudes_de_credito.csv", index_col=0, sep=";")

    str_cols = ["barrio", "línea_credito", "idea_negocio", "monto_del_credito"]

    df.sexo = df.sexo.str.lower()
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()
    df.monto_del_credito = df.monto_del_credito.str.replace(".00", "").str.replace("[,. $]", "", regex=True)
    df[str_cols] = df[str_cols].apply(lambda col: col.str.lower().str.replace("[-_]", " ", regex=True))
    df.fecha_de_beneficio = df.fecha_de_beneficio.apply(convertir_fecha)
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    # df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio, format="%Y/%m/%d", errors="coerce")

    pd.set_option("display.max_rows", None)
    print(df.fecha_de_beneficio.value_counts().shape[0])

    df.to_csv(os.path.join(output_dir, output_file), index=False, sep=";")


pregunta_01()
