# 🎫 Sistema de análisis de tickets (PNL)
Bienvenido a la documentación oficial del Sistema de Análisis de Tickets de Soporte. Este proyecto utiliza técnicas de Procesamiento de Lenguaje Natural para automatizar la clasificación y el diagnóstico de incidencias técnicas.

# 🎯 Objetivos del ProyectoAutomatización: 

- Clasificar tickets de soporte de manera eficiente sin intervención manual constante.
- Análisis Inteligente: Utilizar modelos de NLP para extraer la intención y la urgencia de los mensajes de los usuarios.
- Modularidad: Mantener una estructura limpia que permita escalar el sistema fácilmente.

# 📂 Estructura de Documentación
Para facilitar la navegación, la documentación se divide en las siguientes secciones:

|Sección | Descripción |
| :--- | :--- | 
|Arquitectura| Detalles sobre el flujo de datos y la interacción entre módulos (src/). |
|Referencia API| Documentación técnica de funciones en preprocess.py, nlp_analyzer.py y pipeline.py. |
|Guía de Usuario| Instrucciones sobre cómo ejecutar el sistema y entender los reportes generados. |
|Guía de Desarrollo| Estándares de código, configuración del entorno y ejecución de tests con pytest. |

# 🚀 Inicio Rápido
Si ya tienes el entorno configurado, puedes iniciar el análisis principal ejecutando:

Pasos previos recomendados:

- Activar el entorno virtual: Asegúrate de tener tu venv activo.

- Verificar variables: Revisa que tu archivo .env contenga las rutas correctas a los modelos de NLP.

- Ejecutar pruebas: Antes de procesar datos reales, confirma que todo esté en orden.