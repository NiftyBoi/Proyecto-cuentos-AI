import logging
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.units import cm
import os


class PDFGenerator:
    """Genera un PDF con texto e imagen de la historia."""

    @staticmethod
    def create_pdf(
        folder: str, cuento_texto: str, image_path: str, filename="cuento.pdf"
    ):
        path = os.path.join(folder, filename)
        c = canvas.Canvas(path, pagesize=A4)
        width, height = A4

        # Márgenes
        margin_x, margin_y = 2 * cm, 2 * cm
        usable_width = width - 2 * margin_x

        # Título
        c.setFont("Helvetica-Bold", 18)
        c.drawCentredString(width / 2, height - margin_y, "Mini Historia")

        # Imagen
        if image_path and os.path.exists(image_path):
            img = ImageReader(image_path)
            img_height = 8 * cm
            img_width = usable_width
            c.drawImage(
                img,
                margin_x,
                height - margin_y - img_height - 30,
                width=img_width,
                height=img_height,
                preserveAspectRatio=True,
                mask="auto",
            )
            texto_y = height - margin_y - img_height - 40
        else:
            texto_y = height - margin_y - 40

        # Texto
        styles = getSampleStyleSheet()
        style = styles["Normal"]
        style.fontSize = 12
        style.leading = 15
        story = [
            Paragraph(line, style) for line in cuento_texto.split("\n") if line.strip()
        ]

        frame = Frame(
            margin_x, margin_y, usable_width, texto_y - margin_y, showBoundary=0
        )
        frame.addFromList(story, c)
        c.save()

        logging.info(f"PDF generado en: {path}")
        return path
