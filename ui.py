import os
from tkinter import filedialog
import customtkinter as ctk

# Importamos tus componentes existentes
from csv_analyzer import CsvAnalyzer
from csv_loader import CsvLoader  # Cambiar a CsvLoader si renombraste la clase
from csv_report import CsvReportGenerator

# Configuración estética global de la aplicación
ctk.set_appearance_mode("System")  # Detecta si el PC usa modo oscuro o claro
ctk.set_default_color_theme("blue")  # Tema de color principal


class AppAnalizador(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("📊 Media Intelligence Analyzer")
        self.geometry("600x500")
        self.resizable(False, False)

        self.ruta_archivo_seleccionado = ""

        # --- DISEÑO DE LA INTERFAZ ---

        # 1. Título Principal
        self.lbl_titulo = ctk.CTkLabel(
            self,
            text="Analizador de Menciones en Medios",
            font=ctk.CTkFont(size=22, weight="bold"),
        )
        self.lbl_titulo.pack(pady=(20, 20))

        # 2. SECCIÓN: Selección de Archivo
        self.frame_archivo = ctk.CTkFrame(self)
        self.frame_archivo.pack(pady=10, padx=40, fill="x")

        self.btn_buscar = ctk.CTkButton(
            self.frame_archivo,
            text="Seleccionar CSV",
            command=self.seleccionar_archivo,
            width=140,
        )
        self.btn_buscar.grid(row=0, column=0, padx=10, pady=10)

        self.lbl_archivo = ctk.CTkLabel(
            self.frame_archivo,
            text="No se ha seleccionado ningún archivo...",
            text_color="gray",
            anchor="w",
        )
        self.lbl_archivo.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.frame_archivo.columnconfigure(1, weight=1)

        # 3. SECCIÓN: Palabra Clave (Filtro)
        self.frame_filtro = ctk.CTkFrame(self)
        self.frame_filtro.pack(pady=10, padx=40, fill="x")

        self.lbl_keyword = ctk.CTkLabel(
            self.frame_filtro,
            text="Palabra Clave (Opcional):",
            font=ctk.CTkFont(size=13),
        )
        self.lbl_keyword.grid(row=0, column=0, padx=15, pady=15, sticky="w")

        self.txt_keyword = ctk.CTkEntry(
            self.frame_filtro,
            placeholder_text="Ej: Lumora, servicio, crisis...",
            width=250,
        )
        self.txt_keyword.grid(row=0, column=1, padx=15, pady=15, sticky="e")
        self.frame_filtro.columnconfigure(1, weight=1)

        # 4. Botón de Acción Principal (Ejecutar)
        self.btn_ejecutar = ctk.CTkButton(
            self,
            text="🚀 Procesar y Generar Reporte",
            command=self.procesar_analisis,
            font=ctk.CTkFont(size=14, weight="bold"),
            height=40,
            fg_color="#2c67ad",
        )
        self.btn_ejecutar.pack(pady=20, padx=40, fill="x")

        # 5. SECCIÓN: Consola de Salida de Estado
        self.txt_consola = ctk.CTkTextbox(
            self, width=520, height=180, font=ctk.CTkFont(family="Courier")
        )
        self.txt_consola.pack(pady=(10, 20), padx=40)
        self.escribir_consola(
            "Sistemas listos. Por favor, selecciona un archivo CSV para comenzar."
        )

    # --- LÓGICA DE LA APLICACIÓN ---

    def seleccionar_archivo(self):
        """Abre una ventana nativa del sistema para elegir el archivo CSV."""
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo de menciones",
            filetypes=[("Archivos CSV", "*.csv")],
        )
        if ruta:
            self.ruta_archivo_seleccionado = ruta
            nombre_corto = os.path.basename(ruta)
            self.lbl_archivo.configure(text=nombre_corto, text_color="green")
            self.escribir_consola(f"Archivo cargado: {nombre_corto}")

    def escribir_consola(self, texto: str):
        """Añade texto a la caja de estado inferior simulando una terminal."""
        self.txt_consola.configure(state="normal")
        self.txt_consola.insert("end", texto + "\n")
        self.txt_consola.configure(state="disabled")
        self.txt_consola.see("end")

    def procesar_analisis(self):
        """Conecta la interfaz visual con tu lógica original usando tus clases."""
        if not self.ruta_archivo_seleccionado:
            self.escribir_consola("❌ Error: Debes seleccionar un archivo CSV.")
            return

        palabra_cliente = self.txt_keyword.get().strip()
        if palabra_cliente == "":
            palabra_cliente = None

        try:
            self.escribir_consola("⚡ Iniciando procesamiento...")

            # 1. Carga y Limpieza (Responsabilidad de Csv_loader)
            loader = CsvLoader(self.ruta_archivo_seleccionado)
            datos_limpios = loader.cargar_csv()

            # 2. Procesamiento y Lógica (Responsabilidad de CsvAnalyzer)
            analyzer = CsvAnalyzer(datos_limpios)
            analyzer.filtro(palabra_cliente)

            # 3. Generación del reporte JSON
            reporter = CsvReportGenerator(analyzer, palabra_cliente)
            sufijo = palabra_cliente.lower() if palabra_cliente else "general"

            nombre_json = f"informe_{sufijo}.json"

            reporter.exportar_json(nombre_json)
            
            total_menciones = analyzer.obtener_total_menciones()
            medio_top, alcance_top = analyzer.obtener_top_alcance()

            self.escribir_consola("\n--- ✨ PROCESO COMPLETADO ---")
            self.escribir_consola(f"🔹 Total Menciones: {total_menciones}")
            self.escribir_consola(
                f"🔹 Top Alcance: {medio_top} ({alcance_top:,} imp.)"
            )
            self.escribir_consola(f"💾 Guardado como: {nombre_json}\n")

        except Exception as e:
            self.escribir_consola(f"❌ Ocurrió un error inesperado: {str(e)}")


if __name__ == "__main__":
    app = AppAnalizador()
    app.mainloop()