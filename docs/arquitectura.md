# 🏗️ Arquitectura del Sistema
Este documento describe la estructura lógica y el flujo de datos del Sistema de Análisis de Tickets. El sistema está diseñado bajo un enfoque modular para facilitar el mantenimiento y la escalabilidad de los modelos de NLP.

# 🧩 Descripción de Módulos (src/)
Basado en la estructura del proyecto, el sistema se divide en las siguientes capas funcionales:

## 1. Preprocesamiento ( preprocess.py)
Es la primera etapa del pipeline. Se encarga de la limpieza de los datos crudos para que el modelo de lenguaje pueda entenderlos.

Funciones: Eliminación de ruido (caracteres especiales), tokenización, y normalización de texto.

## 2. Analizador de PLN ( nlp_analyzer.py)
Contiene la inteligencia del sistema. Aquí residen los modelos de procesamiento de lenguaje natural.

Funciones: Clasificación de categorías, detección de sentimiento y extracción de entidades clave del ticket.

## 3. Orquestador (pipeline.py)
Actúa como el pegamento del sistema. Coordina el paso de datos entre el preprocesamiento y el análisis.

Funciones: Ejecución secuencial de tareas y manejo de excepciones durante el flujo de datos.

## 4. Modelos de Datos (models.py)
Define las estructuras de datos (clases/schemas) que representan un Ticket y su Resultado.

Funciones: Validación de tipos y estandarización de la salida del sistema.

## 5. Acciones (actions.py)
Define las operaciones que el sistema puede realizar tras el análisis.

Funciones: Envío de notificaciones, guardado en base de datos o redirección del ticket.

# 🔄 Flujo de Datos
El camino que sigue un ticket desde su entrada hasta su resolución es el siguiente:

- Entrada: El script main.py recibe un ticket crudo.

- Limpieza: preprocess.py transforma el texto en un formato procesable.

- Análisis: nlp_analyzer.py asigna una categoría y prioridad.

- Estructuración: models.py valida que la salida tenga el formato correcto.

- Acción: actions.py ejecuta la respuesta (ej. marcar como "Urgente").

# 🛠️ Tecnologías Utilizadas
Lenguaje: Python 3.x

PNL: (Indicar aquí si usas Spacy, NLTK o Transformers)

Testing: Pytest (ubicado en la carpeta /tests)

CI/CD: GitHub Actions (configurado en .github/workflows/ci.yml)