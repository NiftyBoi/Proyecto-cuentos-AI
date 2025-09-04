class AudioGenerator:
    def __init__(self, openai_service):
        self.openai = openai_service

    def generar_audio(self, texto: str) -> bytes:
        try:
            with self.openai.client.audio.speech.with_streaming_response.create(
                model="gpt-4o-mini-tts", 
                voice="alloy",
                input=texto
            ) as respuesta:
                return respuesta.read()  # devolvemos el binario en memoria
        except Exception as e:
            print(f"\nError al generar audio: {str(e)}")
            return None
