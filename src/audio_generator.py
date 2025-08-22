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
            # Limpiar el tema para el nombre del archivo
            tema_limpio = "".join(c for c in tema if c.isalnum() or c in (' ', '-', '_')).rstrip()
            tema_limpio = tema_limpio.replace(' ', '_')[:20]  # Máximo 20 caracteres
            
            nombre_archivo = f"{tema_limpio}_{nivel}_{timestamp}.mp3"
            ruta_completa = os.path.join(self.audio_dir, nombre_archivo)

            # Verificar que el modelo TTS sea correcto
            respuesta = self.client.audio.speech.create(
                model="tts-1",  # Modelo correcto para TTS
                voice="alloy",  # Otras opciones: echo, fable, onyx, nova, shimmer
                input=texto,
                speed=1.0  # Velocidad normal (0.25 a 4.0)
            )

            # Escribir el archivo de audio
            respuesta.stream_to_file(ruta_completa)

            print(f"\n✅ Audio generado exitosamente: {ruta_completa}")
            return ruta_completa

        except Exception as e:
            print(f"\nError al generar audio: {str(e)}")
            return None

    def listar_audios(self):
        """Lista todos los audios generados"""
        if not os.path.exists(self.audio_dir):
            return []
        
        audios = [f for f in os.listdir(self.audio_dir) if f.endswith('.mp3')]
        return sorted(audios)

    def eliminar_audio(self, nombre_archivo: str):
        """Elimina un archivo de audio específico"""
        ruta = os.path.join(self.audio_dir, nombre_archivo)
        try:
            if os.path.exists(ruta):
                os.remove(ruta)
                print(f"Audio eliminado: {nombre_archivo}")
                return True
            else:
                print(f"Audio no encontrado: {nombre_archivo}")
                return False
        except Exception as e:
            print(f"Error al eliminar audio: {str(e)}")
            return False