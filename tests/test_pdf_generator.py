from PIL import Image


def test_pdf_generator_with_image(tmp_path):
    # Crear una imagen de prueba real
    image_path = tmp_path / "test.jpg"
    img = Image.new("RGB", (100, 100), color="blue")
    img.save(image_path, "JPEG")

    cuento_texto = "Título: El perro feliz\nHabía una vez un perro llamado Bruno..."
    folder = tmp_path

    from src.core.utils.pdf_generator import PDFGenerator

    pdf_path = PDFGenerator.create_pdf(str(folder), cuento_texto, str(image_path))

    assert pdf_path.endswith("cuento.pdf")
    assert tmp_path.joinpath("cuento.pdf").exists()
