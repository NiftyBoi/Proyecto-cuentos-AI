import logging
from core.cuento import Cuento


class AudioGenerator:
    """
    Clase que genera el audio narrado de un cuento usando la API de OpenAI.
    """

    def __init__(self, openai_service):
        self.openai = openai_service

    def generar(self, cuento: Cuento) -> bytes:
        """
        Genera un archivo de audio narrando el texto del cuento.

        Args:
            cuento (Cuento): Objeto que contiene el texto del cuento.

        Returns:
            bytes: Audio en formato binario si tiene éxito, None si falla.
        """
        logging.info(f"Iniciando generación de audio para el cuento: '{cuento.tema}'.")

        try:
            # Llamada a la API de OpenAI
            with self.openai.client.audio.speech.with_streaming_response.create(
                model="gpt-4o-mini-tts",
                voice="alloy",  # Voz estándar para la narración
                input=cuento.texto,
            ) as respuesta:

                audio_data = respuesta.read()

                # Validación de la respuesta
                if not audio_data or len(audio_data) == 0:
                    logging.error("La API devolvió un audio vacío o nulo.")
                    return None

                logging.info("Audio generado exitosamente.")
                return audio_data

        except ConnectionError:
            logging.error(
                "Fallo de conexión durante la generación de audio.", exc_info=True
            )
            return None
        except TimeoutError:
            logging.error(
                "Tiempo de espera excedido al generar el audio.", exc_info=True
            )
            return None
        except Exception as e:
            logging.critical(
                f"Error inesperado al generar el audio: {e}", exc_info=True
            )
            return None
