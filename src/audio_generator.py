import os
from datetime import datetime
from openai import OpenAI

class AudioGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        # Crear carpeta de audios si no existe
        self.audio_dir = "audios_cuentos"
        os.makedirs(self.audio_dir, exist_ok=True)

    def generar_audio(self, texto: str, tema: str = "cuento", nivel: str = "1"):
        try:
            # Crear nombre único basado en tema, nivel y timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            tema_limpio = "".join(c for c in tema if c.isalnum() or c in (' ', '-', '_')).rstrip()
            tema_limpio = tema_limpio.replace(' ', '_')[:20]
            
            nombre_archivo = f"{tema_limpio}_{nivel}_{timestamp}.mp3"
            ruta_completa = os.path.join(self.audio_dir, nombre_archivo)

            respuesta = self.client.audio.speech.create(
                model="gpt-4o-mini-tts", 
                voice="alloy",
                input=texto
            )

            audio_bytes = respuesta.read()

            with open(ruta_completa, "wb") as f:
                f.write(audio_bytes)

            print(f"\nAudio generado: {ruta_completa}")
            return ruta_completa

        except Exception as e:
            print(f"\nError al generar audio: {str(e)}")
            return None