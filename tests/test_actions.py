from src.actions import ejecutar_accion_segun_ticket
from src.models import TicketAnalizado, CategoriaTicket, UrgenciaTicket

def test_ejecutar_accion_segun_ticket_prints_correctly(capsys):
    # 1. Preparar un ticket de prueba
    ticket = TicketAnalizado(
        texto_original="Mi app no funciona",
        categoria=CategoriaTicket.TECNICO,
        urgencia=UrgenciaTicket.ALTA,
        intencion="Reportar error",
        accion_sugerida="Escalar a soporte"
    )

    # 2. Ejecutar la función
    ejecutar_accion_segun_ticket(ticket)

    # 3. Capturar la salida de la consola
    captured = capsys.readouterr()

    # 4. Aserciones (Verificar que el texto aparece en consola)
    assert "ACCIÓN AUTOMATIZADA LOCAL" in captured.out
    assert "tecnico" in captured.out
    assert "ALTA" in captured.out
    assert "Escalar a soporte" in captured.out

def test_ejecutar_accion_segun_ticket_different_category(capsys):
    # Test secundario para asegurar cobertura total con otra categoría
    ticket = TicketAnalizado(
        texto_original="Quiero un reembolso",
        categoria=CategoriaTicket.FACTURACION,
        urgencia=UrgenciaTicket.BAJA,
        intencion="Reclamar pago",
        accion_sugerida="Revisar factura"
    )
    
    ejecutar_accion_segun_ticket(ticket)
    captured = capsys.readouterr()
    
    assert "facturacion" in captured.out
    assert "BAJA" in captured.out