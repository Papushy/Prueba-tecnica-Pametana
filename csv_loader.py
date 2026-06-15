import pandas
import os
class CsvLoader:
    def __init__ (self, ruta_archivo:str):
        self.ruta_archivo=ruta_archivo


    def cargar_csv(self)-> pandas.DataFrame:

        if not os.path.exists(self.ruta_archivo):
            raise FileNotFoundError(f"El archivo {self.ruta_archivo} no existe")
        
        archivo_csv=pandas.read_csv(self.ruta_archivo)

        return self.limpiar_csv(archivo_csv)
    
    def limpiar_csv(self,archivo_csv):
        archivo_csv["medio"] = archivo_csv["medio"].fillna("Sin Medio")

        archivo_csv["fecha"]=pandas.to_datetime(archivo_csv["fecha"],format="mixed",dayfirst=True).dt.strftime("%Y-%m-%d")

        archivo_csv["alcance"]=(pandas.to_numeric(archivo_csv["alcance"],errors="coerce").fillna(0).astype(int))

        return archivo_csv