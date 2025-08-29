from core.cuento import CuentoGenerator
from services.openai_service import OpenAIService
from core.utils import normalizar_nivel

def main():
    # Inicializamos el servicio OpenAI
    openai_service = OpenAIService()
    cuento_gen = CuentoGenerator(openai_service)

    # Pedimos datos al usuario
    tema = input("Ingrese el tema del cuento: ").strip()
    nivel = pedir_nivel()

    # Generamos el cuento
    cuento = cuento_gen.generar_cuento(tema, nivel)
    print("\nAquí tienes tu cuento:\n")
    print(cuento)


def pedir_nivel():
    while True:
        # Primero pedimos el nivel al usuario
        nivel_usuario= input("Ingresa el nivel educativo (ej: 1, primero, 2° básico, 3° básico o 4° básico): ").strip()
        
        try:
            # Intentamos normalizar el nivel
            nivel_normalizado = normalizar_nivel(nivel_usuario)
            return nivel_normalizado
        except ValueError as e:
            # Si hay error en la normalización, mostramos el mensaje y pedimos de nuevo
            print(f"{e}")





if __name__ == "__main__":
    main()
