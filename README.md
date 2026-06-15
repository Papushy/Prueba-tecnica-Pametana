# Analizador de Menciones en Medios con Pandas

Este proyecto es una herramienta en Python diseñada para automatizar el procesamiento, limpieza y análisis estadístico de impactos en medios de comunicación a partir de un archivo de origen CSV. 

La aplicación permite calcular métricas clave de rendimiento, aplicar filtros dinámicos por palabras clave (como nombres de clientes) y exportar los resultados tanto a la terminal como a un informe estructurado en formato JSON.

---

## 🚀 Cómo Ejecutar el Proyecto

### 1. Requisitos Previos
Asegúrate de tener instalado Python (versión 3.8 o superior) y las librerías `pandas , customtkinters`. Si no tienes las librerías, puedes instalarlas ejecutando:

bash
pip install pandas customtkinter


### 2. Estructura de archivos
Todos los archivos .py deben estar en el mismo directorio

### 3. Ejecucion 
Ejecutaremos el script ui.py abrira una interfaz visual donde buscaremos el csv y pondremos la palabra clave (si no hay palabra clave se hará el reporte de todo) 

---

## Decisiones tomadas

### 1. Eleccion de libreria para el analisis
He hecho una pequeña investigacion para ver que libreria me facilitaria el trabajo en este caso es pandas que trata archivos como el csv de manera similar a una base de datos

### 2. Modularizar el codigo
En este caso he dividido en 3 clases distintas el trabajo del script esto para no saturar de codigo un solo archivo .py y a la hora de gestionar cambios o errores sea mas sencillo buscar

### 3. Exportacion de reporte 
He decidido exportarlo tanto en consola para ver que los datos esten correctos como desarrollador, como en JSON
### 4. Interfaz visual
Para no tener que modificar el codigo cada vez que haya cambios en el archivo o en la palabra clave he creado una interfaz visual esta nos valdra para una ejecucion manual del script

---

## Mejoras futuras

### Tipos de consultas
Añadiria mas tipos de consultas para poder sacar mas datos

### Base de Datos
Guardaria la informacion del csv en una base de datos en la nube para que la informacion siempre este disponible sin importar el dispositivo asi en caso de en un futuro tener 
otro tipo de informacion relacionada con este csv sea solo añadir nuevas tablas a nuestra BBDD.
