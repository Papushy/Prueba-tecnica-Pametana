import json
from csv_analyzer import CsvAnalyzer
from datetime import datetime


class CsvReportGenerator:

    def __init__(self, analizador: CsvAnalyzer, palabra_clave: str = None):
        self.analizador = analizador
        self.palabra_clave = palabra_clave

    def _estructura_reporte(self) -> dict:
        medio_top, alcance_top = self.analizador.obtener_top_alcance()

        estructura = {
            "configuracion": {
                "palabra_clave_buscada": (
                    self.palabra_clave
                    if self.palabra_clave
                    else "Ninguna (Todo el archivo)"
                ),
                "total_menciones_encontradas": self.analizador.obtener_total_menciones(),
            },
            "metricas": {
                "medio_mayor_alcance": {
                    "medio": medio_top,
                    "alcance_acumulado": alcance_top,
                },
                "menciones_por_medio": self.analizador.obtener_menciones_medio(),
                "menciones_por_fecha": self.analizador.obtener_menciones_fecha(),
            },
        }
        return estructura

    def imprimir_en_consola(self):
        datos = self._estructura_reporte()
        config = datos["configuracion"]
        metricas = datos["metricas"]

        print("=" * 60)
        print("📊 INFORME DE MENCIONES EN MEDIOS")
        print(f"   Filtro aplicado: {config['palabra_clave_buscada']}")
        print("=" * 60)
        print(
            f"🔹 Número total de menciones: {config['total_menciones_encontradas']}"
        )

        medio_top = metricas["medio_mayor_alcance"]["medio"]
        alcance_top = metricas["medio_mayor_alcance"]["alcance_acumulado"]
        print(
            f"🔹 Medio con mayor alcance : {medio_top} ({alcance_top:,} impactos)"
        )

        print("\n📈 Menciones por medio:")
        for medio, cantidad in metricas["menciones_por_medio"].items():
            print(f"   - {medio:18}: {cantidad} noticia(s)")

        print("\n📅 Menciones por día:")
        for fecha, cantidad in metricas["menciones_por_fecha"].items():
            print(f"   - {fecha}: {cantidad} noticia(s)")
        print("=" * 60 + "\n")

    def exportar_json(self, ruta_archivo: str):
        # 🗓️ Metemos la fecha de hoy automáticamente en el nombre
        fecha_hoy = datetime.now().strftime("%Y-%m-%d")
        nombre, extension = ruta_archivo.rsplit(".", 1)
        ruta_con_fecha = f"{nombre}_{fecha_hoy}.{extension}"

        datos = self._estructura_reporte()
        with open(ruta_con_fecha, "w", encoding="utf-8") as reporte:
            json.dump(datos, reporte, ensure_ascii=False, indent=4)

        print(f"💾 Informe JSON exportado con éxito a: {ruta_con_fecha}")
