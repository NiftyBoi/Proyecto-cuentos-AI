import sys
import logging
from core.cuento import CuentoGenerator
from core.audio import AudioGenerator
from core.imagen import ImagenGenerator
from core.utils.file_manager import FileManager
from core.utils.normalizador import NivelNormalizer
from core.utils.pdf_generator import PDFGenerator


class CuentoApp:
    """Orquesta el flujo de generación de cuentos, audios, imágenes y PDF."""

    def __init__(self, openai_service):
        self.openai = openai_service
        self.cuento_gen = CuentoGenerator(openai_service)
        self.audio_gen = AudioGenerator(openai_service)
        self.imagen_gen = ImagenGenerator(openai_service)
        self.file_manager = FileManager()
        self.pdf_generator = PDFGenerator()
        logging.info("CuentoApp inicializada correctamente.")

    def run(self):
        tema = self.pedir_input("Ingrese el tema del cuento (o 'salir'): ")
        nivel = self.pedir_nivel()
        logging.info(f"Generando cuento para nivel {nivel} sobre el tema '{tema}'")

        # Generar cuento
        cuento = self.cuento_gen.generar(tema, nivel)
        logging.debug(f"Cuento generado: {cuento.texto[:100]}...")

        # Generar imagen y audio
        cuento.imagen = self.imagen_gen.generar(cuento)
        cuento.audio = self.audio_gen.generar(cuento)
        logging.info("Imagen y audio generados correctamente.")

        # Guardar outputs
        carpeta = self.file_manager.create_story_folder(cuento.tema)
        ruta_txt = self.file_manager.save_text(carpeta, cuento.texto)
        ruta_img = self.file_manager.save_image(carpeta, cuento.imagen)
        ruta_pdf = self.pdf_generator.create_pdf(carpeta, cuento.texto, ruta_img)
        ruta_audio = self.file_manager.save_audio(carpeta, cuento.audio)

        logging.info(f"Archivos guardados en la carpeta: {carpeta}")
        logging.info(f"Texto guardado en: {ruta_txt}")
        logging.info(f"Imagen guardada en: {ruta_img}")
        logging.info(f"PDF guardado en: {ruta_pdf}")
        logging.info(f"Audio guardado en: {ruta_audio}")

    def pedir_input(self, mensaje: str) -> str:
        valor = input(mensaje).strip()
        if valor.lower() in ["salir", "exit", "q"]:
            logging.warning("El usuario decidió salir de la aplicación.")
            print("Saliendo...")
            sys.exit(0)
        return valor

    def pedir_nivel(self) -> str:
        while True:
            nivel_usuario = self.pedir_input(
                "Ingresa el nivel educativo (desde 1ro a 4to basico): "
            )
            try:
                return NivelNormalizer.normalizar(nivel_usuario)
            except ValueError as e:
                logging.error(f"Nivel educativo inválido ingresado: {nivel_usuario}")
                print(e)
