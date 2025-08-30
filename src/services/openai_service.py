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

