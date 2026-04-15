# 🛠️ Guía de Desarrollo
Esta guía está destinada a desarrolladores y contribuidores que deseen configurar el entorno de trabajo, ejecutar pruebas o añadir nuevas funcionalidades al sistema.

## ⚙️ Configuración del Entorno
Para garantizar la consistencia entre entornos, sigue estos pasos:

- Clonar el repositorio:

- Crear un entorno virtual:

-Instalar dependencias:
    Utiliza el archivo de requerimientos visible en la raíz del proyecto:

- Variables de Entorno:
    Copia el archivo de ejemplo o crea uno nuevo llamado .env basándote en la configuración necesaria para el proyecto.

## 🧪 Ejecución de Pruebas (Tests)
El proyecto utiliza pytest para asegurar la calidad del código. La estructura de pruebas se encuentra en la carpeta tests/.

- Ejecutar todos los tests:

- Ejecutar con reporte de cobertura:
    Asegúrate de cubrir los módulos críticos como nlp_analyzer.py y pipeline.py:

# 📏 Estándares de Código
Para mantener la legibilidad y el orden, todos los contribuidores deben adherirse a las siguientes normas:

## 🐍 Estilo de Python

- Seguir la guía de estilo PEP 8.

- Utilizar Docstrings claros en cada función y clase nueva dentro de src/, detallando parámetros y valores de retorno.

- Evitar dependencias circulares entre los módulos de lógica (preprocess, nlp_analyzer, actions).

## 📝 Commits Semánticos
Utilizamos el estándar de Conventional Commits para el historial de Git:

- feat: Nueva funcionalidad.

- fix: Corrección de un error.

- docs: Cambios en la documentación.

- test: Añadir o modificar pruebas.

- refactor: Cambios en el código que no corrigen errores ni añaden funciones.

## 🚀 Tubería de CI/CD
El proyecto cuenta con una configuración de Integración Continua en .github/workflows/ci.yml.

- Cualquier Pull Request enviado debe pasar automáticamente las siguientes comprobaciones:

- Instalación exitosa de dependencias.

- Validación de sintaxis y estilo (Linter).

- Ejecución exitosa de la suite de pruebas completa.