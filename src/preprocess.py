import re

def preprocesar_texto(texto: str, max_caracteres: int = 5000) -> str:
    """Limpia el texto de etiquetas HTML y caracteres no deseados."""
    texto = re.sub(r'<[^>]+>', '', texto)
    texto = re.sub(r'\s+', ' ', texto).strip()
    texto = re.sub(r'[\x00-\x1f\x7f]', '', texto)
    return texto[:max_caracteres]