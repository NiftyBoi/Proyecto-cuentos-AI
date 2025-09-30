import logging


class Cuento:
    """
    Representa un cuento generado por la IA.
    Atributos:
        tema (str): Tema del cuento
        nivel (str): Nivel educativo
        texto (str): Texto completo del cuento
    """

    def __init__(self, tema: str, nivel: str, texto: str, audio=None, imagen=None):
        self.tema = tema
        self.nivel = nivel
        self.texto = texto
        self.audio = audio
        self.imagen = imagen

    def __repr__(self):
        return f"Cuento(tema='{self.tema}', nivel='{self.nivel}', texto='{self.texto[:30]}...')"


class CuentoGenerator:
    """
    Genera cuentos a partir de un tema y nivel educativo usando OpenAI.
    """

    def __init__(self, openai_service):
        self.openai = openai_service

    def generar(self, tema: str, nivel: str) -> Cuento:
        logging.info(
            f"Iniciando generación de cuento. Tema: '{tema}', Nivel: '{nivel}'"
        )

        try:
            prompt = (
                f"Escribe un cuento para niños de {nivel} "
                f"cuyo tema central sea: {tema}. "
                "Los personajes y la trama deben estar relacionados con este tema. "
                "Incluye un título que empiece con 'Título:' y "
                "termina el cuento con un párrafo "
                "que empiece con 'Y desde ese día' o 'Así aprendieron que'."
            )

            logging.debug(f"Prompt enviado a OpenAI: {prompt}")

            # Llamada al servicio de OpenAI
            texto = self.openai.generar_texto(prompt)

            # Validación de la respuesta
            if not texto or len(texto.strip()) == 0:
                logging.error("OpenAI devolvió un texto vacío o nulo.")
                raise ValueError("No se generó texto para el cuento.")

            logging.info("Cuento generado exitosamente.")
            return Cuento(tema, nivel, texto)

        except Exception as e:
            # Registro detallado del error
            logging.error(f"Error al generar el cuento: {e}", exc_info=True)
            raise  # Relanza el error para que la capa superior lo maneje
