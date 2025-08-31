from core.cuento import CuentoGenerator
from core.audio import AudioGenerator
from services.openai_service import OpenAIService
from core.utils import normalizar_nivel
from core.imagen import ImagenGenerator
import sys  # para poder usar sys.exit()

def main():
    # Inicializamos el servicio OpenAI
    openai_service = OpenAIService()
    
    cuento_gen = CuentoGenerator(openai_service)
    audio_gen = AudioGenerator(openai_service)
    imagen_gen = ImagenGenerator(openai_service)

    # Pedimos datos al usuario
    tema = pedir_input("Ingrese el tema del cuento (O escribe salir para terminar el programa): ")
    nivel = pedir_nivel()

    # Generamos el cuento
    cuento = cuento_gen.generar_cuento(tema, nivel)
    print("\nAquí tienes tu cuento:\n")
    print(cuento)

    # Generamos el audio del cuento
    ruta_audio = audio_gen.generar_audio(cuento, tema, nivel)
    if ruta_audio:
        print(f"\nNarración guardada en: {ruta_audio}")

    # Generamos la imagen del cuento
    ruta_imagen = imagen_gen.generar_cuento(cuento, tema, nivel)
    if ruta_imagen:
        print(f"\nImagen guardada en: {ruta_imagen}")


def pedir_input(mensaje: str) -> str:
    #funcion que permite al usuario salir del programa en cualquier input
    valor = input(mensaje).strip()
    if valor.lower() in ["salir", "exit", "q"]:
        print("👋 Saliendo del programa...")
        sys.exit(0)
    return valor


def pedir_nivel():
    while True:
        nivel_usuario = pedir_input("Ingresa el nivel educativo (ej: 1, primero, 2° básico, 3° básico o 4° básico): ")
        try:
            nivel_normalizado = normalizar_nivel(nivel_usuario)
            return nivel_normalizado
        except ValueError as e:
            print(f"{e}")


if __name__ == "__main__":
    main()
