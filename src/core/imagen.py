import os
import base64
from datetime import datetime

class ImagenGenerator:
    def __init__(self, openai_service):
        self.openai = openai_service
        # Crear carpeta de audios si no existe
        self.imagen_dir = "imagenes_cuentos"
        os.makedirs(self.imagen_dir, exist_ok=True)

    def generar_cuento(self, texto: str, tema: str, nivel: str):
        try:
            # Crear nombre único basado en tema, nivel y timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            tema_limpio = "".join(c for c in tema if c.isalnum() or c in (' ', '-', '_')).rstrip()
            tema_limpio = tema_limpio.replace(' ', '_')[:20]
            
            nombre_archivo = f"{tema_limpio}_{nivel}_{timestamp}.jpg"
            ruta_completa = os.path.join(self.imagen_dir, nombre_archivo)

            # Prompt para la imagen (puede mejorar con más detalles)
            prompt = f"Ilustración infantil colorida para un cuento sobre {tema}, nivel {nivel}. Estilo de libro ilustrado para niños."

            # Generar la imagen usando el servicio OpenAI
            respuesta = self.openai.client.images.generate(
                model="gpt-image-1",
                prompt=prompt,
                size="1024x1024"
            )

            #La Api devuelve la imagen en base64
            image_base64 = respuesta.data[0].b64_json
            image_bytes = base64.b64decode(image_base64)

            #guardar la imagen en un archivo
            with open(ruta_completa, "wb") as img_file:
                img_file.write(image_bytes)
            return ruta_completa


        except Exception as e:
            print(f"\nError al generar imagen: {str(e)}")
            return None
