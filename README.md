# Sistema de Análisis de Tickets de Soporte con NLP

## Descripción
Este proyecto es una herramienta avanzada para la gestión de incidencias técnicas. Utiliza técnicas de Procesamiento de Lenguaje Natural (NLP) para automatizar la clasificación de tickets, determinar su prioridad mediante análisis de sentimiento y facilitar la respuesta rápida del equipo de soporte.

## Instalación
Sigue estos pasos para configurar el entorno local:

Intento
### 1. Clonar el repositorio
git clone https://github.com/tu-usuario/SISTEMA_TICKETS.git
cd SISTEMA_TICKETS

### 2. Crear y activar el entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows use: venv\Scripts\activate

### 3. Instalar las dependencias
pip install -r requirements.txt

## Variables de entorno
Crea un archivo .env en la raíz del proyecto para configurar el sistema:

- LOG_LEVEL: Nivel de detalle de los logs (DEBUG, INFO, ERROR).

- MODEL_PATH: Ruta local al modelo de lenguaje pre-entrenado.

- API_KEY: Credencial necesaria para servicios externos (si aplica).

## Usar
Para ejecutar el flujo principal de análisis de tickets, utiliza el script principal ubicado en la raíz:

Intento
python main.py

## Estructura del proyecto
La organización del repositorio es la siguiente:
```
SISTEMA_TICKETS/
├── .github/
│   └── workflows/
│       └── ci.yml             # Pipeline de Integración Continua (GitHub Actions)
├── docs/                      # Documentación completa del proyecto
│   ├── api_reference.md
│   ├── arquitectura.md
│   ├── development.md
│   ├── index.md
│   └── user_guide.md
├── Heredado/                  # Versiones antiguas o scripts de referencia
│   ├── app.py
│   └── appV1.py
├── src/                       # Lógica principal del sistema
│   ├── __init__.py
│   ├── actions.py             # Definición de acciones/respuestas
│   ├── models.py              # Definición de modelos de datos
│   ├── nlp_analyzer.py        # Procesamiento de lenguaje natural
│   ├── pipeline.py            # Orquestación del flujo de datos
│   └── preprocess.py          # Limpieza y normalización de texto
├── tests/                     # Suite de pruebas unitarias
│   ├── __init__.py
│   ├── test_pipeline.py
│   └── test_preprocess.py
├── .env                       # Variables de entorno y secretos
├── .gitignore                 # Archivos excluidos de Git
├── conftest.py                # Configuración global para Pytest
├── LICENSE                    # Licencia del software
├── main.py                    # Punto de entrada de la aplicación
├── practica.md                # Guía de práctica o notas internas
├── pytest.ini                 # Parámetros de configuración de tests
├── readme_Informe.md          # Informe técnico detallado
├── README.md                  # Presentación general del repositorio
├── requirements.txt           # Dependencias de Python
└── setup.cfg                  # Ajustes de empaquetado y linters
```

# Pruebas

Para garantizar la calidad del código, ejecuta la suite de pruebas con el reporte de cobertura de la siguiente manera:

Intento

## Ejecutar tests con cobertura en la carpeta src

pytest --cov=src tests/

## Canalización de CI
El proyecto integra GitHub Actions a través del archivo ci.yml. En cada push o pull request, el pipeline realiza:

- Verificación de sintaxis (Linting).

- Instalación automática de dependencias.

- Ejecución de la suite completa de tests.

# Licencia
Este proyecto se distribuye bajo la Licencia MIT. Consulta el archivo LICENSE para más información.