from core.cuento import CuentoGenerator
from services.openai_service import OpenAIService

def main():
    openai_service = OpenAIService()

    cuento_gen = CuentoGenerator(openai_service)

    cuento = cuento_gen.generar_cuento("animales del bosque", "2° básico")
    print(cuento)


if __name__ == "__main__":
    main()
