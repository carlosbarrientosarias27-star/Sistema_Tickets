from src.models import TicketAnalizado

def ejecutar_accion_segun_ticket(ticket: TicketAnalizado) -> None:
    """Lógica de respuesta automatizada basada en el análisis."""
    print("\n" + "⚡ ACCIÓN AUTOMATIZADA LOCAL")
    print(f"Prioridad: {ticket.urgencia.value.upper()} | Canal: {ticket.categoria.value}")
    print(f"Sugerencia: {ticket.accion_sugerida}")