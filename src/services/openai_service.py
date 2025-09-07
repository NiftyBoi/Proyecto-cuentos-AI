import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class OpenAIService:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generar_texto(self, user_prompt: str, temperature: float = 0.5, max_tokens: int = 700) -> str:

        #Envía el `user_prompt` al modelo como message de usuario.
        #Retorna el texto generado (limpio).
        try:
            # Mensaje system con reglas generales y de seguridad / estilo
            system_msg = (
                "Eres un asistente que escribe cuentos para niños en educación básica. "
                "Usa un lenguaje sencillo, frases cortas y vocabulario apropiado para el grado. "
                "Siempre incluye un desenlace claro y un párrafo final que empiece con "
                "'Y desde ese día' o 'Así aprendieron que'."
            )

            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )

            texto = response.choices[0].message.content.strip()
            return texto

        except Exception as e:
            print(f"[OpenAIService] Error al generar texto: {e}")
            return None
    
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