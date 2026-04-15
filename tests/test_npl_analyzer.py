from unittest.mock import patch
from src.nlp_analyzer import analizar_ticket_con_nlp

# El parche ahora debe apuntar a ollama.chat, que es lo que importa tu nlp_analyzer
@patch('src.nlp_analyzer.ollama.chat')
def test_analizar_ticket_exito(mock_ollama_chat):
    # 1. Configuramos el Mock para simular la respuesta de Ollama
    mock_ollama_chat.return_value = {
        'message': {
            'content': '{"categoria": "tecnico", "urgencia": "alta", "intencion": "test", "accion_sugerida": "test"}'
        }
    }

    # 2. Ejecución
    resultado = analizar_ticket_con_nlp("Mi PC no enciende")

    # 3. Verificación
    assert resultado["exito"] is True
    assert resultado["analisis"]["categoria"] == "tecnico"
    assert resultado["modelo"] == "qwen2.5:7b"