from src.core.cuento import CuentoGenerator, Cuento


class FakeOpenaiService:
    def generar_texto(self, prompt: str) -> str:
        return (
            "Título: El gato aventurero\n"
            "Había una vez un gato llamdo Tonela que vivía en un pequeño pueblo."
            "Y desde ese día, Tonela decidió explorar el mundo."
        )


def test_generar_cuento():
    fake_openai = FakeOpenaiService()
    generator = CuentoGenerator(fake_openai)

    cuento = generator.generar("gatos", "1° básico")

    assert isinstance(cuento, Cuento)
    assert "gatos" in cuento.tema.lower()

    # validar el titulo correcto
    assert cuento.texto.startswith("Título:")

    # validar que el cuento termine correctamente
    assert cuento.texto.strip().endswith(
        "Y desde ese día, Tonela decidió explorar el mundo."
    )
