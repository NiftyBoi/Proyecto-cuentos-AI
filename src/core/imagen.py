class ImagenGenerator:
    def __init__(self, openai_service):
        self.openai = openai_service

    def generar_imagen(self, tema: str, nivel: str) -> bytes:
        try:
            prompt = f"Ilustración infantil colorida para un cuento sobre {tema}, nivel {nivel}. Estilo libro ilustrado."
            respuesta = self.openai.client.images.generate(
                model="gpt-image-1",
                prompt=prompt,
                size="1024x1024"
            )
            return respuesta.data[0].b64_json  # devolvemos el base64, no lo guardamos aquí
        except Exception as e:
            print(f"\nError al generar imagen: {str(e)}")
            return None
