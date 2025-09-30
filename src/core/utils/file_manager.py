import os
import re
import base64
import logging
from datetime import datetime


class FileManager:
    def __init__(self, base_dir="outputs"):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)

    def sanitize_filename(self, name: str) -> str:
        """Limpia nombres inválidos para archivos y carpetas."""
        safe = re.sub(r'[<>:"/\\|?*]', "_", name)
        safe = safe.replace(" ", "_").lower()
        return safe

    def create_story_folder(self, title: str) -> str:
        """Crea una carpeta única para cada cuento."""
        safe_title = self.sanitize_filename(title)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        folder_name = f"{safe_title}_{timestamp}"
        path = os.path.join(self.base_dir, folder_name)
        os.makedirs(path, exist_ok=True)
        logging.info(f"Carpeta creada para cuento: {path}")
        return path

    def save_file(self, folder: str, content: bytes, filename: str, mode: str = "wb"):
        """Método genérico para guardar cualquier archivo."""
        path = os.path.join(folder, filename)
        with open(path, mode) as f:
            f.write(content)
        logging.info(f"Archivo guardado: {path}")
        return path

    def save_text(self, folder: str, content: str, filename="cuento.txt"):
        return self.save_file(folder, content.encode("utf-8"), filename, mode="wb")

    def save_image(self, folder: str, image_base64: str, filename="cuento.jpg"):
        image_bytes = base64.b64decode(image_base64)
        return self.save_file(folder, image_bytes, filename)

    def save_audio(self, folder: str, audio_bytes: bytes, filename="cuento.mp3"):
        return self.save_file(folder, audio_bytes, filename)
