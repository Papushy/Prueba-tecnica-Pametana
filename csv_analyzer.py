import pandas
from transformers import pipeline
class CsvAnalyzer:
    def __init__(self, dataframe: pandas.DataFrame):
        self.dataframe_original=dataframe
        self.dataframe_filtrado=dataframe.copy()

        self.clasificador_ia = pipeline(
            "sentiment-analysis",
            model="pysentimiento/robertuito-sentiment-analysis",
        )

    def analizar_sentimiento_menciones(self) -> dict:
        if self.dataframe_filtrado.empty:
            return {"POS": 0, "NEU": 0, "NEG": 0}

        # Extraemos los titulares como una lista de texto
        titulares = self.dataframe_filtrado["titular"].astype(str).tolist()

        # La IA procesa todos los titulares de golpe
        resultados_ia = self.clasificador_ia(titulares)

        # Extraemos las etiquetas de los resultados (POS, NEU, NEG)
        lista_sentimientos = [res["label"] for res in resultados_ia]

        # Añadimos los resultados como una nueva columna en nuestro DataFrame filtrado
        self.dataframe_filtrado["sentimiento"] = lista_sentimientos

        # Contamos cuántos hay de cada uno y lo devolvemos como diccionario
        conteo = self.dataframe_filtrado["sentimiento"].value_counts().to_dict()

        # Aseguramos que el diccionario tenga las 3 opciones aunque alguna valga 0
        return {
            "Positivo": conteo.get("POS", 0),
            "Neutro": conteo.get("NEU", 0),
            "Negativo": conteo.get("NEG", 0),
        }

    def filtro(self,palabra_clave:str=None):
        
        if palabra_clave:
            filtro=self.dataframe_original["titular"].str.contains(palabra_clave,case=False,na=False)|self.dataframe_original["texto"].str.contains(palabra_clave,case=False,na=False)
            self.dataframe_filtrado=self.dataframe_original[filtro]
        else:
            self.dataframe_filtrado=self.dataframe_original.copy()

    def obtener_total_menciones(self):
        return len(self.dataframe_filtrado)
    
    def obtener_menciones_medio(self):
        return self.dataframe_filtrado["medio"].value_counts().to_dict()
    
    def obtener_menciones_fecha(self):
        return self.dataframe_filtrado["fecha"].value_counts().sort_index().to_dict()
    
    def obtener_top_alcance(self):
        alcance_por_medio=self.dataframe_filtrado.groupby("medio")["alcance"].sum()

        if not alcance_por_medio.empty:
            medio=alcance_por_medio.idxmax()
            valor= int(alcance_por_medio.max())
            return medio, valor
        return "Ninguno",0