import os
import json
import re
import ollama
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional, Tuple

# ============================================
# CONFIGURACIÓN LOCAL
# ============================================
MODEL_NAME = "qwen2.5:7b"

# ============================================
# MODELOS DE DATOS
# ============================================

class CategoriaTicket(Enum):
    CUENTA = "cuenta"
    TECNICO = "tecnico"
    FACTURACION = "facturacion"
    PRODUCTO = "producto"
    OTRO = "otro"

class UrgenciaTicket(Enum):
    ALTA = "alta"
    MEDIA = "media"
    BAJA = "baja"

class TicketAnalizado:
    def __init__(self, texto_original: str, categoria: CategoriaTicket, 
                 urgencia: UrgenciaTicket, intencion: str, 
                 accion_sugerida: str, entidades: Dict = None):
        self.texto_original = texto_original
        self.categoria = categoria
        self.urgencia = urgencia
        self.intencion = intencion
        self.accion_sugerida = accion_sugerida
        self.entidades = entidades or {}
        self.fecha_analisis = datetime.now()
    
    def to_dict(self) -> Dict:
        return {
            "texto_original": self.texto_original[:100] + "..." if len(self.texto_original) > 100 else self.texto_original,
            "categoria": self.categoria.value,
            "urgencia": self.urgencia.value,
            "intencion": self.intencion,
            "accion_sugerida": self.accion_sugerida,
            "entidades": self.entidades,
            "fecha_analisis": self.fecha_analisis.isoformat()
        }

# ============================================
# PREPROCESAMIENTO
# ============================================

def preprocesar_texto(texto: str, max_caracteres: int = 5000) -> str:
    texto = re.sub(r'<[^>]+>', '', texto)
    texto = re.sub(r'\s+', ' ', texto).strip()
    texto = re.sub(r'[\x00-\x1f\x7f]', '', texto)
    return texto[:max_caracteres]

# ============================================
# PROMPT PARA OLLAMA (Ajustado para Qwen 2.5)
# ============================================

SYSTEM_PROMPT_CLASIFICACION = """Eres un experto en soporte técnico. 
Analiza el ticket y responde EXCLUSIVAMENTE con un objeto JSON válido.
Categorías permitidas: ["cuenta", "tecnico", "facturacion", "producto", "otro"]
Urgencias permitidas: ["alta", "media", "baja"]

Estructura JSON:
{
  "categoria": "...",
  "urgencia": "...",
  "intencion": "...",
  "accion_sugerida": "...",
  "entidades": {"email": "...", "pedido_id": "..."}
}"""

# ============================================
# LLAMADA A OLLAMA
# ============================================

def analizar_ticket_con_nlp(texto_usuario: str) -> Dict:
    texto_limpio = preprocesar_texto(texto_usuario)
    
    try:
        # Llamada a Ollama usando el cliente local
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {'role': 'system', 'content': SYSTEM_PROMPT_CLASIFICACION},
                {'role': 'user', 'content': f"Analiza este ticket: {texto_limpio}"},
            ],
            options={'temperature': 0} # Queremos respuestas deterministas
        )
        
        respuesta_texto = response['message']['content']
        
        # Limpieza de posibles tags de Markdown que Qwen a veces incluye (```json ... ```)
        respuesta_texto = re.sub(r'```json\s?|\s?```', '', respuesta_texto).strip()
        
        try:
            resultado = json.loads(respuesta_texto)
            return {
                "exito": True,
                "analisis": resultado,
                "modelo": MODEL_NAME
            }
            
        except json.JSONDecodeError:
            return {
                "exito": False,
                "error": "El modelo local no generó un JSON válido",
                "respuesta_raw": respuesta_texto
            }
            
    except Exception as e:
        return {"exito": False, "error": str(e)}

# ============================================
# TRANSFORMACIÓN Y ACCIONES (Sin cambios significativos)
# ============================================

def transformar_a_ticket(texto_usuario: str, resultado_api: Dict) -> TicketAnalizado:
    analisis = resultado_api.get("analisis", {})
    
    cat_str = analisis.get("categoria", "otro").lower()
    urg_str = analisis.get("urgencia", "media").lower()
    
    # Mapeo robusto
    categoria = next((c for c in CategoriaTicket if c.value == cat_str), CategoriaTicket.OTRO)
    urgencia = next((u for u in UrgenciaTicket if u.value == urg_str), UrgenciaTicket.MEDIA)
    
    return TicketAnalizado(
        texto_original=texto_usuario,
        categoria=categoria,
        urgencia=urgencia,
        intencion=analisis.get("intencion", "No especificada"),
        accion_sugerida=analisis.get("accion_sugerida", "Revisar manualmente"),
        entidades=analisis.get("entidades", {})
    )

def ejecutar_accion_segun_ticket(ticket: TicketAnalizado) -> None:
    print("\n" + "⚡ ACCIÓN AUTOMATIZADA LOCAL")
    print(f"Prioridad: {ticket.urgencia.value.upper()} | Canal: {ticket.categoria.value}")
    print(f"Sugerencia: {ticket.accion_sugerida}")

# ============================================
# PIPELINE Y MAIN
# ============================================

def pipeline_procesamiento_ticket(texto_usuario: str) -> Optional[TicketAnalizado]:
    print(f"\n--- Procesando con {MODEL_NAME} ---")
    resultado = analizar_ticket_con_nlp(texto_usuario)
    
    if not resultado["exito"]:
        print(f"❌ Error: {resultado.get('error')}")
        return None
    
    ticket = transformar_a_ticket(texto_usuario, resultado)
    ejecutar_accion_segun_ticket(ticket)
    return ticket

def main():
    print(f"🚀 Sistema de Tickets Local (Ollama: {MODEL_NAME})")
    
    while True:
        print("\n1. Procesar ticket")
        print("2. Salir")
        opcion = input("> ")
        
        if opcion == "1":
            texto = input("Describe el problema: ")
            pipeline_procesamiento_ticket(texto)
        elif opcion == "2":
            break

if __name__ == "__main__":
    main()