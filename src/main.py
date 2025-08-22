from utils import normalizar_nivel
from cuento_generator import generar_cuento

def main():
    while True:
        print("\n--- Generador de Cuentos ---")
        tema = input("Ingrese el tema del cuento (o 'salir' para terminar): ")

        if tema.lower() == "salir":
            print("Programa finalizado. ¡Hasta la próxima!")
            break

        nivel_input = input("Ingrese el nivel (ej: 1, 1° básico, primero, etc.): ")

        try:
            nivel = normalizar_nivel(nivel_input)
        except ValueError as e:
            print(f"{e}")
            continue

        cuento = generar_cuento(tema, nivel)
        print("\n--- Cuento generado ---\n")
        print(cuento)

if __name__ == "__main__":
    main()
