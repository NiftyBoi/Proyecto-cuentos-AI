import os
import requests
from datetime import datetime
from openai import OpenAI


def generar_imagen(descripcion: str, cuento: str, nivel: str) -> str:
    """
    Genera una imagen usando la API de OpenAI a partir de la descripción, el cuento y el nivel proporcionados.
    Retorna el path de la imagen generada o una cadena vacía si hay error.
    """
    try:
        # Crear cliente OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
        # Crear carpeta de imágenes si no existe
        imagen_dir = "imagenes_cuentos"
        os.makedirs(imagen_dir, exist_ok=True)
        
        # Extraer tema del cuento (primeras palabras como aproximación)
        tema = " ".join(cuento.split()[:5]) if cuento else "cuento"
        
        # Crear nombre único basado en tema, nivel y timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        tema_limpio = "".join(c for c in tema if c.isalnum() or c in (' ', '-', '_')).rstrip()
        tema_limpio = tema_limpio.replace(' ', '_')[:20]
        
        nombre_archivo = f"img_{tema_limpio}_{nivel}_{timestamp}.png"
        ruta_completa = os.path.join(imagen_dir, nombre_archivo)

        # Crear prompt para la imagen
        prompt = (
            f"Genera una imagen para niños basada en la siguiente escena: '{descripcion}'. "
            f"Esta escena es parte de un cuento para estudiantes de {nivel}. "
            f"El cuento trata sobre: {tema}. "
            "La imagen debe ser colorida, amigable y apropiada para niños pequeños. "
            "No debe contener elementos violentos ni inapropiados. "
            "El estilo debe ser ilustración infantil, alegre y llamativa, como un libro de cuentos."
        )

        print("🎨 Generando imagen... por favor espera")

        respuesta = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1024x1024",
            quality="standard",
            style="vivid"
        )

        # Obtener la URL de la imagen
        image_url = respuesta.data[0].url
        
        # Descargar la imagen
        image_response = requests.get(image_url)
        image_bytes = image_response.content

        # Guardar la imagen
        with open(ruta_completa, "wb") as f:
            f.write(image_bytes)
            
        return ruta_completa

    except Exception as e:
        print(f"\nError al generar imagen: {str(e)}")
        return ""