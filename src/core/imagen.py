import logging
from core.cuento import Cuento


class ImagenGenerator:
    """
    Clase encargada de generar ilustraciones para un cuento usando la API de OpenAI.
    """

    def __init__(self, openai_service):
        self.openai = openai_service

    def generar(self, cuento: Cuento) -> str:
        """
        Genera una imagen en base a un cuento dado.

        Args:
            cuento (Cuento): Objeto con tema y nivel educativo.

        Returns:
            str: Imagen codificada en base64 si tiene éxito, None si falla.
        """
        logging.info(f"Iniciando generación de imagen para el tema '{cuento.tema}'.")

        try:
            # Construcción correcta del prompt
            prompt = (
                f"Ilustración infantil colorida para un cuento sobre {cuento.tema}, "
                f"nivel {cuento.nivel}. Estilo libro ilustrado, "
                "amigable y atractivo para niños."
            )

            logging.debug(f"Prompt para imagen: {prompt}")

            # Llamada a la API de OpenAI
            respuesta = self.openai.client.images.generate(
                model="gpt-image-1", prompt=prompt, size="1024x1024"
            )

            # Validar respuesta
            if not respuesta or not respuesta.data:
                logging.error(
                    "La API de OpenAI devolvió una respuesta vacía al generar imagen."
                )
                return None

            logging.info("Imagen generada exitosamente.")
            return respuesta.data[0].b64_json

        except ConnectionError:
            logging.error(
                "Fallo de conexión al intentar generar la imagen.", exc_info=True
            )
            return None
        except TimeoutError:
            logging.error(
                "Tiempo de espera excedido al generar la imagen.", exc_info=True
            )
            return None
        except Exception as e:
            logging.critical(f"Error inesperado al generar imagen: {e}", exc_info=True)
            return None
