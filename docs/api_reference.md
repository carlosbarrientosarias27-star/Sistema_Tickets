# 📚 Referencia de la API
Esta página contiene la documentación técnica detallada de los módulos, clases y funciones que componen el núcleo del Sistema de Análisis de Tickets.

## 🛠️ Módulo: Preprocesamiento (src/preprocess.py)
Encargado de la limpieza y normalización del texto de entrada.

- clean_text(text: str) -> str:

    Recibe una cadena de texto cruda.

    Elimina caracteres especiales, números y convierte todo a minúsculas.

- tokenize(text: str) -> list:

    Divide el texto en una lista de palabras individuales (tokens).

- remove_stopwords(tokens: list) -> list:

    Filtra palabras comunes que no aportan valor semántico (ej: "el", "de", "un").

## 🧠 Módulo: Analizador NLP (src/nlp_analyzer.py)
Contiene la lógica de inteligencia artificial y procesamiento de lenguaje.

- classify_ticket(cleaned_text: str) -> str:

    Predice la categoría del ticket (ej: "Soporte Técnico", "Facturación").

- get_priority_level(text: str) -> str:

    Analiza palabras clave y sentimiento para asignar una prioridad (Baja, Media, Alta).

- extract_keywords(text: str) -> list:

    Identifica términos técnicos o productos específicos mencionados.

## ⛓️ Módulo: Pipeline (src/pipeline.py)
Orquestador del flujo de datos del sistema.

- run_analysis_pipeline(raw_data: dict) -> dict:

    Coordina la ejecución secuencial: Preprocesamiento ➡️ Análisis ➡️ Formateo.

    Retorna un diccionario estructurado con el diagnóstico completo.

## 📁 Módulo: Modelos (src/models.py)
Definición de esquemas de datos.

- class Ticket:

    Estructura base para la entrada de datos (ID, usuario, descripción).

- class AnalysisResult:

    Estructura para la salida del sistema (categoría, prioridad, confianza).

## ⚡ Módulo: Acciones (src/actions.py)
Operaciones post-análisis.

- route_ticket(analysis: dict):

    Determina a qué departamento enviar el ticket basado en el resultado del análisis.

- save_to_database(data: dict):

    Persiste el ticket y su análisis en el sistema de almacenamiento.