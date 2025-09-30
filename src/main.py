import logging
import os
from services.openai_service import OpenAIService
from app import CuentoApp

# Crear carpeta separada SOLO para logs
os.makedirs("logs", exist_ok=True)

# Configurar logging global
logging.basicConfig(
    level=logging.DEBUG,  # DEBUG para desarrollo, INFO para producción
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="logs/app.log",
    filemode="a",  # "a" mantiene el historial, "w" sobrescribe
)

if __name__ == "__main__":
    try:
        logging.info("=== Iniciando aplicación de generación de cuentos ===")
        app = CuentoApp(OpenAIService())
        app.run()
        logging.info("=== Aplicación finalizada correctamente ===")
    except Exception as e:
        logging.critical(f"Error crítico en la aplicación: {e}", exc_info=True)
        print(
            "Ocurrió un error grave. Revisa el archivo logs/app.log para más detalles."
        )
