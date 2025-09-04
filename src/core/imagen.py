from core.cuento import Cuento

class ImagenGenerator:
   # Genera una ilustración para un cuento.
    def __init__(self, openai_service):
        self.openai = openai_service

    def generar(self, cuento: Cuento) -> str:
        try:
            prompt = f"Ilustración infantil colorida para un cuento sobre {cuento.tema}, nivel {cuento.nivel}. Estilo libro ilustrado."
            respuesta = self.openai.client.images.generate(
                model="gpt-image-1",
                prompt=prompt,
                size="1024x1024"
            )
            return respuesta.data[0].b64_json
        except Exception as e:
            print(f"\nError al generar imagen: {str(e)}")
            return None
