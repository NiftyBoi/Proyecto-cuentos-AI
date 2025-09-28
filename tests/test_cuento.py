import pytest
from src.core.cuento import CuentoGenerator, Cuento


class FakeOpenAIService:
    """Simula la respuesta de OpenAI sin llamar a la API real"""
    def generar_texto(self, prompt: str):
        return "Título: El gato feliz\nEste es un cuento ficticio para pruebas."

def test_cuento_generator_crea_cuento():
    # Usamos el servicio falso en lugar de OpenAI real
    fake_openai = FakeOpenAIService()
    generator = CuentoGenerator(fake_openai)

    cuento = generator.generar("gatos", "2° básico")

    assert isinstance(cuento, Cuento)
    assert cuento.tema == "gatos"
    assert cuento.nivel == "2° básico"
    assert isinstance(cuento.texto, str)
    assert len(cuento.texto) > 0
