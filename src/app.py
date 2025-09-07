import sys
from core.cuento import CuentoGenerator
from core.audio import AudioGenerator
from core.imagen import ImagenGenerator
from core.utils import NivelNormalizer, OutputManager

class CuentoApp:

    #Orquesta el flujo de generación de cuentos, audios, imágenes y PDF.

    def __init__(self, openai_service):
        self.openai = openai_service
        self.cuento_gen = CuentoGenerator(openai_service)
        self.audio_gen = AudioGenerator(openai_service)
        self.imagen_gen = ImagenGenerator(openai_service)
        self.output = OutputManager()

    def run(self):
        tema = self.pedir_input("Ingrese el tema del cuento (o 'salir'): ")
        nivel = self.pedir_nivel()

        # Generar cuento
        cuento = self.cuento_gen.generar(tema, nivel)

        # Generar imagen y audio
        cuento.imagen = self.imagen_gen.generar(cuento)
        cuento.audio = self.audio_gen.generar(cuento)

        # Guardar outputs
        carpeta = self.output.create_story_folder(cuento.tema)
        ruta_txt = self.output.save_text(carpeta, cuento.texto)
        ruta_img = self.output.save_image(carpeta, cuento.imagen)
        ruta_pdf = self.output.save_pdf(carpeta, cuento.texto, ruta_img)
        ruta_audio = self.output.save_audio(carpeta, cuento.audio)

        print(f"\nArchivos guardados en: {carpeta}")
        print(f"- Texto: {ruta_txt}")
        print(f"- Imagen: {ruta_img}")
        print(f"- PDF: {ruta_pdf}")
        print(f"- Audio: {ruta_audio}")

    def pedir_input(self, mensaje: str) -> str:
        valor = input(mensaje).strip()
        if valor.lower() in ["salir", "exit", "q"]:
            print("Saliendo...")
            sys.exit(0)
        return valor

    def pedir_nivel(self) -> str:
        while True:
            nivel_usuario = self.pedir_input("Ingresa el nivel educativo (desde 1ro a 4to basico): ")
            try:
                return NivelNormalizer.normalizar(nivel_usuario)
            except ValueError as e:
                print(e)
