import logging


class NivelNormalizer:
    """Convierte la entrada del usuario a un nivel estándar de básico."""

    equivalencias = {
        "1": "1° básico",
        "1ro": "1° básico",
        "primero": "1° básico",
        "1°": "1° básico",
        "primer": "1° básico",
        "2": "2° básico",
        "2do": "2° básico",
        "segundo": "2° básico",
        "2°": "2° básico",
        "3": "3° básico",
        "3ro": "3° básico",
        "tercero": "3° básico",
        "3°": "3° básico",
        "4": "4° básico",
        "4to": "4° básico",
        "cuarto": "4° básico",
        "4°": "4° básico",
    }

    @classmethod
    def normalizar(cls, nivel_usuario: str) -> str:
        nivel_usuario = nivel_usuario.strip().lower()
        if nivel_usuario in cls.equivalencias:
            logging.debug(
                f"Nivel normalizado correctamente: {nivel_usuario} "
                "-> {cls.equivalencias[nivel_usuario]}"
            )
            return cls.equivalencias[nivel_usuario]
        else:
            logging.warning(f"Nivel inválido ingresado: {nivel_usuario}")
            raise ValueError("Nivel inválido. Intente con 1, 2, 3 o 4.")
