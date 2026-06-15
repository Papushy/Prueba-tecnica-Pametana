import pandas

class CsvAnalyzer:
    def __init__(self, dataframe: pandas.DataFrame):
        self.dataframe_original=dataframe
        self.dataframe_filtrado=dataframe.copy()

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