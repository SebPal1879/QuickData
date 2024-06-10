import pandas as pd
import os


def archivo_a_xlsx(nombre):
    ruta_actual = os.path.dirname(__file__)
    ruta_archivo_csv = os.path.join(ruta_actual,'archivos_csv', nombre+".csv")
    read_file = pd.read_csv(ruta_archivo_csv,encoding='UTF-8')
    ruta_archivo_xlsx = os.path.join(ruta_actual,'archivos_xlsx', nombre+".xlsx")
    read_file.to_excel(ruta_archivo_xlsx,index = None, header=True)

