import os
import re
import base64
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.units import cm


class NivelNormalizer:
    #Convierte la entrada del usuario a un nivel estándar de básico.
    equivalencias = {
        "1": "1° básico", "1ro": "1° básico", "primero": "1° básico", "1°": "1° básico", "primer": "1° básico",
        "2": "2° básico", "2do": "2° básico", "segundo": "2° básico", "2°": "2° básico",
        "3": "3° básico", "3ro": "3° básico", "tercero": "3° básico", "3°": "3° básico",
        "4": "4° básico", "4to": "4° básico", "cuarto": "4° básico", "4°": "4° básico",
    }

    @classmethod
    def normalizar(cls, nivel_usuario: str) -> str:
        nivel_usuario = nivel_usuario.strip().lower()
        if nivel_usuario in cls.equivalencias:
            return cls.equivalencias[nivel_usuario]
        else:
            raise ValueError("Nivel inválido. Intente con 1, 2, 3 o 4.")


class OutputManager:
    #Se encarga de guardar y organizar los archivos generados (texto, audio, imagen, PDF).

    def __init__(self, base_dir="outputs"):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)

    def sanitize_filename(self, name: str) -> str:
        #Elimina caracteres inválidos para nombres en Windows/Linux/macOS.
        safe = re.sub(r'[<>:"/\\|?*]', "_", name)  # reemplaza caracteres prohibidos
        safe = safe.replace(" ", "_").lower()
        return safe

    def create_story_folder(self, title: str) -> str:
        safe_title = self.sanitize_filename(title)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        folder_name = f"{safe_title}_{timestamp}"
        path = os.path.join(self.base_dir, folder_name)
        os.makedirs(path, exist_ok=True)
        return path

    def save_text(self, folder: str, content: str, filename="cuento.txt"):
        path = os.path.join(folder, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return path

    def save_audio(self, folder: str, audio_bytes: bytes, filename="cuento.mp3"):
        path = os.path.join(folder, filename)
        with open(path, "wb") as f:
            f.write(audio_bytes)
        return path

    def save_image(self, folder: str, image_base64: str, filename="cuento.jpg"):
        path = os.path.join(folder, filename)
        image_bytes = base64.b64decode(image_base64)
        with open(path, "wb") as f:
            f.write(image_bytes)
        return path

    def save_pdf(self, folder: str, cuento_texto: str, image_path: str, filename="cuento.pdf"):
        path = os.path.join(folder, filename)
        c = canvas.Canvas(path, pagesize=A4)
        width, height = A4

        # Márgenes
        margin_x, margin_y = 2 * cm, 2 * cm
        usable_width = width - 2 * margin_x
        usable_height = height - 2 * margin_y

        # Título
        c.setFont("Helvetica-Bold", 18)
        c.drawCentredString(width / 2, height - margin_y, "Mini Historia")

        # Imagen
        if image_path and os.path.exists(image_path):
            img = ImageReader(image_path)
            img_height = 8 * cm
            img_width = usable_width
            c.drawImage(img, margin_x, height - margin_y - img_height - 30,
                        width=img_width, height=img_height, preserveAspectRatio=True, mask='auto')
            texto_y = height - margin_y - img_height - 40
        else:
            texto_y = height - margin_y - 40

        # Texto con salto de línea automático
        styles = getSampleStyleSheet()
        style = styles["Normal"]
        style.fontName = "Helvetica"
        style.fontSize = 12
        style.leading = 15

        story = [Paragraph(line, style) for line in cuento_texto.split("\n") if line.strip()]

        frame = Frame(margin_x, margin_y, usable_width, texto_y - margin_y, showBoundary=0)
        frame.addFromList(story, c)

        c.save()
        return path
