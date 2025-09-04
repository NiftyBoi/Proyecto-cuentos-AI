from core.cuento import Cuento

class AudioGenerator:
    #Genera el audio narrado de un cuento.
    def __init__(self, openai_service):
        self.openai = openai_service

    def generar(self, cuento: Cuento) -> bytes:
        try:
            with self.openai.client.audio.speech.with_streaming_response.create(
                model="gpt-4o-mini-tts", 
                voice="alloy",
                input=cuento.texto
            ) as respuesta:
                return respuesta.read()
        except Exception as e:
            print(f"\nError al generar audio: {str(e)}")
            return None
