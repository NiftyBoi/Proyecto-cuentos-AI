class Cuento:
    #Representa un cuento generado, con sus datos asociados.
    def __init__(self, tema: str, nivel: str, texto: str, audio=None, imagen=None):
        self.tema = tema
        self.nivel = nivel
        self.texto = texto
        self.audio = audio
        self.imagen = imagen

class CuentoGenerator:
    #Genera cuentos a partir de un tema y nivel educativo usando OpenAI.
    def __init__(self, openai_service):
        self.openai = openai_service

    def generar(self, tema: str, nivel: str) -> Cuento:
        prompt = f"Genera un cuento para niños de {nivel} sobre {tema}"
        texto = self.openai.generar_texto(prompt)
        return Cuento(tema, nivel, texto)
