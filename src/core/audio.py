import os
from datetime import datetime

class AudioGenerator:
    def __init__(self, openai_service):
        self.openai = openai_service
        # Crear carpeta de audios si no existe
        self.audio_dir = "audios_cuentos"
        os.makedirs(self.audio_dir, exist_ok=True)

    def generar_audio(self, texto: str, tema: str, nivel: str):
        try:
            # Crear nombre único basado en tema, nivel y timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            tema_limpio = "".join(c for c in tema if c.isalnum() or c in (' ', '-', '_')).rstrip()
            tema_limpio = tema_limpio.replace(' ', '_')[:20]
            
            nombre_archivo = f"{tema_limpio}_{nivel}_{timestamp}.mp3"
            ruta_completa = os.path.join(self.audio_dir, nombre_archivo)

            # Generar el audio usando el servicio OpenAI
            with self.openai.client.audio.speech.with_streaming_response.create(
                model="gpt-4o-mini-tts", 
                voice="alloy",
                input=texto
            ) as respuesta:
                respuesta.stream_to_file(ruta_completa)

            return ruta_completa

        except Exception as e:
            print(f"\nError al generar audio: {str(e)}")
            return None
