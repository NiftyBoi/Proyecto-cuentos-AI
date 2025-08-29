class ImagenGenerator:
    def __init__(self, openai_service):
        self.openai = openai_service

    def generar_imagen(self, descripcion: str, output_path: str):
        return self.openai.generar_imagen(descripcion, output_path)
