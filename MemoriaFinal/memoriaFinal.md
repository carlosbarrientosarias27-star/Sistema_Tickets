# Memoria de Refactorización: Sistema de Tickets NLP

## 1. Análisis del Código Original (`app.py`)
El código heredado presentaba varios problemas de diseño conocidos como "Code Smells" (hedores de código):

* **Violación del Principio de Responsabilidad Única (SRP):** El archivo `app.py` era un "Objeto Todopoderoso". Gestionaba desde la carga de variables de entorno y la limpieza de texto hasta la lógica de negocio, llamadas a la API y el menú de usuario.
* **Baja Mantenibilidad:** Cualquier cambio en la lógica de OpenAI o en las categorías de los tickets obligaba a modificar el mismo archivo donde reside la interfaz de usuario.
* **Dificultad para Testing:** Al estar todas las funciones acopladas en un solo script, era imposible realizar tests unitarios aislados sin disparar ejecuciones completas o llamadas reales a la API.
* **Escalabilidad Limitada:** No permitía reutilizar componentes (como el preprocesador) en otros proyectos de forma sencilla.

## 2. Cambios Realizados y Justificación

Para mejorar la calidad del software, se aplicó una arquitectura modular dividiendo el proyecto en la carpeta `src/`:

### A. Modularización (Carpeta `src/`)
1.  **`models.py`**: Se extrajeron los `Enum` y la clase `TicketAnalizado`. Esto centraliza la definición de datos y evita errores de tipado.
2.  **`preprocess.py`**: Se aisló la lógica de limpieza de texto (Regex). Ahora es una utilidad pura que puede testearse sin dependencias externas.
3.  **`nlp_analyzer.py`**: Se encapsuló la comunicación con OpenAI. Esto permite cambiar de modelo (ej. de GPT-4o-mini a Claude) modificando un solo archivo.
4.  **`actions.py`**: Se separó la lógica de negocio (qué hacer con cada ticket). Esto facilita añadir nuevas reglas de soporte en el futuro.
5.  **`pipeline.py`**: Se implementó una clase orquestadora que une todas las piezas, permitiendo un flujo de datos controlado y fácil de depurar.

### B. Implementación de Tests (Carpeta `tests/`)
Se implementaron pruebas automatizadas con `pytest` para garantizar que la refactorización no rompió la funcionalidad original (Regression Testing), logrando una cobertura superior al 80%.

### C. Despliegue y CI/CD
* Se añadió `.github/workflows/ci.yml` para automatizar las pruebas en cada `push`.
* Se configuró un entorno profesional con `requirements.txt`, `.env` y `setup.cfg`.

## 3. Conclusión
La nueva estructura no solo cumple con los requisitos técnicos, sino que transforma un script monolítico en una **aplicación de grado de producción** lista para ser mantenida y escalada por un equipo de desarrollo.