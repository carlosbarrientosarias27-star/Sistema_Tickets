import ollama
import json
import re
from typing import Dict, Any

MODEL_NAME = "qwen2.5:7b"
SYSTEM_PROMPT = """Eres un experto en soporte técnico. 
Analiza el ticket y responde EXCLUSIVAMENTE con un objeto JSON válido.
Categorías: ["cuenta", "tecnico", "facturacion", "producto", "otro"]
Urgencias: ["alta", "media", "baja"]

Estructura JSON:
{
  "categoria": "...",
  "urgencia": "...",
  "intencion": "...",
  "accion_sugerida": "...",
  "entidades": {"email": "...", "pedido_id": "..."}
}"""

def analizar_ticket_con_nlp(texto_limpio: str) -> Dict[str, Any]:
    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {'role': 'system', 'content': SYSTEM_PROMPT},
                {'role': 'user', 'content': f"Analiza este ticket: {texto_limpio}"},
            ],
            options={'temperature': 0}
        )
        
        raw_content = response['message']['content']
        # Limpieza de Markdown
        json_str = re.sub(r'```json\s?|\s?```', '', raw_content).strip()
        
        return {
            "exito": True,
            "analisis": json.loads(json_str),
            "modelo": MODEL_NAME
        }
    except Exception as e:
        return {"exito": False, "error": str(e)}