# tests/test_preprocess.py
import pytest
from src.preprocess import preprocesar_texto

def test_limpieza_html():
    input_text = "<p>Error en el <b>servidor</b></p>"
    esperado = "Error en el servidor"
    assert preprocesar_texto(input_text) == esperado

def test_espacios_y_trim():
    input_text = "   usuario@dominio.com    "
    esperado = "usuario@dominio.com"
    assert preprocesar_texto(input_text) == esperado

def test_limite_max_caracteres():
    input_text = "1234567890"
    # Forzamos un límite corto para la prueba
    assert preprocesar_texto(input_text, max_caracteres=5) == "12345"

def test_caracteres_no_deseados():
    # El regex busca [\x00-\x1f\x7f] (caracteres de control ASCII)
    input_text = "Texto\x01con\x02caracteres\x1focultos"
    esperado = "Textoconcaracteres ocultos"
    assert preprocesar_texto(input_text) == esperado

def test_input_vacio():
    assert preprocesar_texto("") == ""