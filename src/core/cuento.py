class CuentoGenerator:
    def __init__(self, openai_service):
        self.openai = openai_service

    def generar_cuento(self, tema: str, nivel: str) -> str:
        prompt = f"Genera un cuento para niños de {nivel} sobre {tema}"
        return self.openai.generar_texto(prompt)
