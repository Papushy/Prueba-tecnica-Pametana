# Analizador de Menciones en Medios con Pandas

Este proyecto es una herramienta en Python diseñada para automatizar el procesamiento, limpieza y análisis estadístico de impactos en medios de comunicación a partir de un archivo de origen CSV. 

La aplicación permite calcular métricas clave de rendimiento, aplicar filtros dinámicos por palabras clave (como nombres de clientes) y exportar los resultados tanto a la terminal como a un informe estructurado en formato JSON.

---

## Cómo Ejecutar el Proyecto

### 1. Requisitos Previos
Asegúrate de tener instalado Python (versión 3.8 o superior) y la librería `pandas`. Si no tienes la librería, puedes instalarla ejecutando:

bash
pip install pandas

### 2. Estructura de archivos
Todos los archivos .py deben estar en el mismo directorio

### 3. Automatizacion de script
Abrimos el programador de tareas y crearemos una nueva tarea diaria de ejecucion y elegiremos ejecutar_analisis.bat a la hora que convenga


---

## Decisiones tomadas

### 1. Eleccion de libreria para el analisis
He hecho una pequeña investigacion para ver que libreria me facilitaria el trabajo en este caso es pandas que trata archivos como el csv de manera similar a una base de datos

### 2. Modularizar el codigo
En este caso he dividido en 3 clases distintas el trabajo del script esto para no saturar de codigo un solo archivo .py y a la hora de gestionar cambios o errores sea mas sencillo buscar

### 3. Exportacion de reporte 
He decidido exportarlo tanto en consola para ver que los datos esten correctos como desarrollador, como en JSON

### 4.Automatizacion
He usado el programador de tareas para no tener que descargar ningun programa externo ademas de la sencillez de uso

---

## Mejoras futuras

### Tipos de consultas
Añadiria mas tipos de consultas para poder sacar mas datos

### Base de Datos
Guardaria la informacion del csv en una base de datos en la nube para que la informacion siempre este disponible sin importar el dispositivo asi en caso de en un futuro tener 
otro tipo de informacion relacionada con este csv sea solo añadir nuevas tablas a nuestra BBDD.

### Tendencia con IA
Que la inteligencia artificial analice y haga el reporte con las palabras claves mas utilizadas en las menciones.