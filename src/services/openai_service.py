import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class OpenAIService:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generar_texto(self, prompt: str) -> str:
        respuesta = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": (
                    "Eres un asistente que escribe cuentos para niños en educación básica. "
                    "El cuento siempre debe tener un desenlace claro y un párrafo final de cierre "
                    "que empiece con 'Y desde ese día...' o 'Así aprendieron que...'."
                )}],
            temperature=0.8,
            max_tokens=700
        )
        return respuesta.choices[0].message.content
    
    def generar_audio(self, texto: str, ruta_salida: str) -> str:
        with self.client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice="alloy",
            input=texto
        ) as respuesta:
            respuesta.stream_to_file(ruta_salida)
        return ruta_salida

    def generar_imagen(self, prompt: str):
        try:
            response = self.client.images.generate(
                model="gpt-image-1",
                prompt=prompt,
                size="1024x1024"
            )
            # Obtienes la imagen en base64 → decodificar a bytes
            import base64
            image_base64 = response.data[0].b64_json
            return base64.b64decode(image_base64)
        except Exception as e:
            print(f"Error en generar_imagen: {e}")
            return None