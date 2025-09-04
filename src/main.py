from services.openai_service import OpenAIService
from app import CuentoApp

if __name__ == "__main__":
    app = CuentoApp(OpenAIService())
    app.run()
