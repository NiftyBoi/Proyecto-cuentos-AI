def normalizar_nivel(nivel_usuario: str) -> str:
    """
    Convierte la entrada del usuario a un formato estándar: "1° básico" ... "4° básico".
    """
    nivel_usuario = nivel_usuario.strip().lower()

    equivalencias = {
        "1": "1° básico",
        "1°": "1° básico",
        "1ro": "1° básico",
        "1ro básico": "1° básico",
        "primer": "1° básico",
        "primer básico": "1° básico",
        "primera": "1° básico",
        "primero": "1° básico",
        "primero básico": "1° básico",
        "primero basico": "1° básico",
        "2": "2° básico",
        "2°": "2° básico",
        "2do": "2° básico",
        "2do básico": "2° básico",
        "segundo": "2° básico",
        "segundo básico": "2° básico",
        "segundo basico": "2° básico",
        "segunda": "2° básico",
        "3": "3° básico",
        "3°": "3° básico",
        "3ro": "3° básico",
        "3ro básico": "3° básico",
        "tercero": "3° básico",
        "tercero básico": "3° básico",
        "tecero basico": "3° básico",
        "3ra": "3° básico",
        "4": "4° básico",
        "4°": "4° básico",
        "4to": "4° básico",
        "4to básico": "4° básico",
        "cuarto": "4° básico",
        "cuarto básico": "4° básico",
        "cuarto basico": "4° básico",
    }

    if nivel_usuario in equivalencias:
        return equivalencias[nivel_usuario]
    else:
        raise ValueError("Nivel inválido. Intente con 1, 2, 3, 4, o sus equivalentes en palabras.")
