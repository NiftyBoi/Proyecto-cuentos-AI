import os
from openai import OpenAI

class AudioGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generar_audio(self, texto: str, nombre_archivo: str = "cuento.mp3"):
        try:
            respuesta = self.client.audio.speech.create(
                model="gpt-4o-mini-tts",
                voice="alloy",
                input=texto
            )

            
            audio_bytes = respuesta.read()

            with open(nombre_archivo, "wb") as f:
                f.write(audio_bytes)

            print(f"\n Audio generado: {nombre_archivo}")
            return nombre_archivo

        except Exception as e:
            print(f"\n Error al generar audio: {str(e)}")
            return None
