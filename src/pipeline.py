from typing import Optional
from src.preprocess import preprocesar_texto
from src.nlp_analyzer import analizar_ticket_con_nlp
from src.models import TicketAnalizado, CategoriaTicket, UrgenciaTicket
from src.actions import ejecutar_accion_segun_ticket

class TicketPipeline:
    def __init__(self):
        print("--- Pipeline Inicializado ---")

    def procesar(self, texto_usuario: str) -> Optional[TicketAnalizado]:
        # 1. Preprocesamiento
        limpio = preprocesar_texto(texto_usuario)
        
        # 2. Análisis NLP
        resultado = analizar_ticket_con_nlp(limpio)
        if not resultado["exito"]:
            print(f"❌ Error en NLP: {resultado.get('error')}")
            return None
        
        # 3. Transformación a Objeto
        data = resultado["analisis"]
        ticket = TicketAnalizado(
            texto_original=texto_usuario,
            categoria=next((c for c in CategoriaTicket if c.value == data.get("categoria")), CategoriaTicket.OTRO),
            urgencia=next((u for u in UrgenciaTicket if u.value == data.get("urgencia")), UrgenciaTicket.MEDIA),
            intencion=data.get("intencion", "N/A"),
            accion_sugerida=data.get("accion_sugerida", "Revisión manual"),
            entidades=data.get("entidades", {})
        )
        
        # 4. Ejecución de acción
        ejecutar_accion_segun_ticket(ticket)
        
        return ticket