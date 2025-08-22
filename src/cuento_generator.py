import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Niveles válidos
NIVELES_VALIDOS = ["1° básico", "2° básico", "3° básico", "4° básico", "1", "2", "3", "4"]

def generar_cuento(tema: str, nivel: str) -> str:
    if not tema or not tema.strip():
        raise ValueError("El tema del cuento no puede estar vacío.")

    if nivel not in NIVELES_VALIDOS:
        raise ValueError(f"Nivel inválido. Debe ser uno de: {', '.join(NIVELES_VALIDOS)}")

    try:
        # Generar cuento principal
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": (
                    "Eres un asistente que escribe cuentos para niños en educación básica. "
                    "Debes escribir cuentos completos de entre 600 y 700 palabras. "
                    "El cuento siempre debe tener un desenlace claro y un párrafo final de cierre "
                    "que empiece con 'Y desde ese día...' o 'Así aprendieron que...'."
                )},
                {"role": "user", "content": f"Escribe un cuento sobre '{tema}' para estudiantes de {nivel}."}
            ],
            max_tokens=850,
            temperature=0.8
        )

        cuento = response.choices[0].message.content.strip()

        # --- Validar si terminó bien ---
        if not (cuento.endswith(".") or cuento.endswith("!") or cuento.endswith("?")):
            continuation = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Continúa el cuento desde donde quedó, "
                                                  "pero SOLO escribe un final claro y feliz para niños."},
                    {"role": "user", "content": cuento}
                ],
                max_tokens=200,
                temperature=0.8
            )
            cuento += " " + continuation.choices[0].message.content.strip()

        return cuento

    except Exception as e:
        print(f"Error al generar el cuento: {str(e)}")
        return "No se pudo generar el cuento en este momento."

