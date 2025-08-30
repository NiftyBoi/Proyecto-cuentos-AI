from core.cuento import CuentoGenerator
from core.audio import AudioGenerator
from services.openai_service import OpenAIService
from core.utils import normalizar_nivel

def main():
    # Inicializamos el servicio OpenAI
    openai_service = OpenAIService()
    
    cuento_gen = CuentoGenerator(openai_service)
    audio_gen = AudioGenerator(openai_service)

    # Pedimos datos al usuario
    tema = input("Ingrese el tema del cuento: ").strip()
    nivel = pedir_nivel()

    # Generamos el cuento
    cuento = cuento_gen.generar_cuento(tema, nivel)
    print("\nAquí tienes tu cuento:\n")
    print(cuento)

    # Generamos el audio del cuento (CORREGIDO: no pisamos cuento)
    ruta_audio = audio_gen.generar_audio(cuento, tema, nivel)
    if ruta_audio:
        print(f"\nNarración guardada en: {ruta_audio}")


def pedir_nivel():
    while True:
        nivel_usuario = input("Ingresa el nivel educativo (ej: 1, primero, 2° básico, 3° básico o 4° básico): ").strip()
        try:
            nivel_normalizado = normalizar_nivel(nivel_usuario)
            return nivel_normalizado
        except ValueError as e:
            print(f"{e}")


if __name__ == "__main__":
    main()
