# 📖 Guía de Usuario: Sistema de Tickets NLP
Esta guía te ayudará a utilizar el sistema para procesar tickets de soporte y entender los análisis generados automáticamente.

## 🚀 Cómo empezar

1. Preparación de los datos
El sistema procesa archivos de texto o datos estructurados. Asegúrate de que tus tickets contengan al menos:
- ID: Un identificador único para el seguimiento.
- Descripción: El texto del problema escrito por el cliente.

2. Ejecución del sistema
Para iniciar el procesamiento de los tickets pendientes, abre tu terminal en la carpeta raíz del proyecto y ejecuta:

Intento
python main.py

## 📥 Cómo subir/cargar tickets
Actualmente, el sistema está configurado para leer desde la fuente definida en tu archivo de configuración local.

- Si usas archivos CSV/JSON: Coloca tus archivos en la carpeta de entrada especificada en el archivo .env.
- Si usas entrada manual: Sigue las instrucciones que aparecerán en la consola tras ejecutar main.py.

# 📊 Interpretación de Resultados
Una vez que el sistema termina el análisis, verás un informe detallado. Aquí te explicamos qué significa cada campo:

| Campo | Descripción | Ejemplo | 
| :--- | :--- | 
|Categoría| El departamento al que se ha asignado el ticket.| Software, Hardware,Redes|
|Prioridad| La urgencia detectada por el análisis de sentimiento.| Baja, Media, Alta,Crítica|
|Confianza| Qué tan seguro está el sistema de su clasificación.| 0.95 (95% de seguridad)|
|Etiquetas| Palabras clave extraídas automáticamente.| login, password,error 404|