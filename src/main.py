from core.cuento import CuentoGenerator
from core.audio import AudioGenerator
from services.openai_service import OpenAIService
from core.utils import normalizar_nivel, OutputManager
from core.imagen import ImagenGenerator
import sys

def main():
    openai_service = OpenAIService()
    
    cuento_gen = CuentoGenerator(openai_service)
    audio_gen = AudioGenerator(openai_service)
    imagen_gen = ImagenGenerator(openai_service)
    manager = OutputManager()

    tema = pedir_input("Ingrese el tema del cuento (O escribe salir): ")
    nivel = pedir_nivel()

    cuento = cuento_gen.generar_cuento(tema, nivel)

    # Crear carpeta única por cuento
    carpeta_cuento = manager.create_story_folder(tema)

    # Guardar cuento como .txt
    ruta_txt = manager.save_text(carpeta_cuento, cuento)

    # Generar imagen y guardar
    imagen_b64 = imagen_gen.generar_imagen(tema, nivel)
    ruta_imagen = manager.save_image(carpeta_cuento, imagen_b64)

    # Generar PDF con texto + imagen
    ruta_pdf = manager.save_pdf(carpeta_cuento, cuento, ruta_imagen)

    # Generar audio y guardar
    audio_bytes = audio_gen.generar_audio(cuento)
    ruta_audio = manager.save_audio(carpeta_cuento, audio_bytes)

    print(f"\nArchivos guardados en: {carpeta_cuento}")
    print(f"- Texto: {ruta_txt}")
    print(f"- Imagen: {ruta_imagen}")
    print(f"- PDF: {ruta_pdf}")
    print(f"- Audio: {ruta_audio}")



def pedir_input(mensaje: str) -> str:
    valor = input(mensaje).strip()
    if valor.lower() in ["salir", "exit", "q"]:
        print("Saliendo...")
        sys.exit(0)
    return valor

def pedir_nivel():
    while True:
        nivel_usuario = pedir_input("Ingresa el nivel educativo: ")
        try:
            return normalizar_nivel(nivel_usuario)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
