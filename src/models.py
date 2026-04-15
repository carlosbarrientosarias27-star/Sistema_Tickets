from enum import Enum
from datetime import datetime
from typing import Dict, Any

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
                 accion_sugerida: str, entidades: Dict[str, Any] = None):
        self.texto_original = texto_original
        self.categoria = categoria
        self.urgencia = urgencia
        self.intencion = intencion
        self.accion_sugerida = accion_sugerida
        self.entidades = entidades or {}
        self.fecha_analisis = datetime.now()
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "texto_original": self.texto_original[:100] + "...",
            "categoria": self.categoria.value,
            "urgencia": self.urgencia.value,
            "intencion": self.intencion,
            "accion_sugerida": self.accion_sugerida,
            "entidades": self.entidades,
            "fecha_analisis": self.fecha_analisis.isoformat()
        }