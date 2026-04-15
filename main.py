from src.pipeline import TicketPipeline

def main():
    pipeline = TicketPipeline()
    print("🚀 Sistema de Tickets Modular Activo")
    
    while True:
        print("\n1. Procesar ticket | 2. Salir")
        opcion = input("> ")
        
        if opcion == "1":
            texto = input("Describe el problema: ")
            pipeline.procesar(texto)
        elif opcion == "2":
            break

if __name__ == "__main__":
    main()