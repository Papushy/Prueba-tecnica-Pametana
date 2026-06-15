from csv_loader import CsvLoader
from csv_analyzer import CsvAnalyzer
from csv_report import CsvReportGenerator


def ejecutar_analisis(archivo_input, palabra_cliente:str=None):
    # 1. Carga y Limpieza (Responsabilidad de Csv_loader)
    loader = CsvLoader(archivo_input)
    datos_limpios = loader.cargar_csv()

    # 2. Procesamiento y Lógica (Responsabilidad de MencionesAnalyzer)
    analyzer = CsvAnalyzer(datos_limpios)
    analyzer.filtro(palabra_cliente)

    # 3. Presentación y Salida (Responsabilidad de ReportGenerator)
    reporter = CsvReportGenerator(analyzer, palabra_cliente)

    # Mostramos en pantalla
    reporter.imprimir_en_consola()

    # Guardamos en archivo con nombre dinámico
    sufijo = palabra_cliente.lower() if palabra_cliente else "general"
    reporter.exportar_json(f"informe_{sufijo}.json")



ejecutar_analisis("menciones.csv")