# tests/test_pipeline.py
import pytest
from unittest.mock import patch, MagicMock
from src.pipeline import TicketPipeline
from src.models import TicketAnalizado, CategoriaTicket

@pytest.fixture
def pipeline():
    return TicketPipeline()

@patch('src.pipeline.analizar_ticket_con_nlp')
@patch('src.pipeline.ejecutar_accion_segun_ticket')
def test_pipeline_flujo_exitoso(mock_accion, mock_nlp, pipeline):
    # Configuramos el mock de NLP
    mock_nlp.return_value = {
        "exito": True,
        "analisis": {
            "categoria": "SOPORTE_TECNICO",
            "urgencia": "ALTA",
            "intencion": "reparación",
            "accion_sugerida": "Escalar a nivel 2",
            "entidades": {"equipo": "laptop"}
        }
    }
    
    resultado = pipeline.procesar("Mi laptop no enciende")
    
    assert isinstance(resultado, TicketAnalizado)
    assert mock_accion.called is True

@patch('src.pipeline.analizar_ticket_con_nlp')
def test_pipeline_error_nlp(mock_nlp, pipeline):
    # Simulamos un fallo en el servicio de NLP
    mock_nlp.return_value = {"exito": False, "error": "Timeout"}
    
    resultado = pipeline.procesar("Hola")
    
    assert resultado is None

@patch('src.pipeline.analizar_ticket_con_nlp')
@patch('src.pipeline.ejecutar_accion_segun_ticket')
def test_pipeline_categoria_por_defecto(mock_accion, mock_nlp, pipeline):
    # Si NLP devuelve una categoría que no existe en el Enum
    mock_nlp.return_value = {
        "exito": True,
        "analisis": {"categoria": "CATEGORIA_INVENTADA", "urgencia": "BAJA"}
    }
    
    resultado = pipeline.procesar("Input extraño")
    
    # Según tu código, si no coincide usa CategoriaTicket.OTRO
    assert resultado.categoria == CategoriaTicket.OTRO