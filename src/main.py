from utils import normalizar_nivel
from cuento_generator import generar_cuento
from audio_generator import AudioGenerator
from imagen_generator import generar_imagen

def main():
    audio_gen = AudioGenerator()  # Crear una sola instancia
    
    while True:
        print("\n--- Generador de Cuentos ---")
        tema = input("Ingrese el tema del cuento (o 'salir' para terminar): ")

        if tema.lower() == "salir":
            print("Programa finalizado. ¡Hasta la próxima!")
            break

        nivel_input = input("Ingrese el nivel (ej: 1, 1° básico, primero, etc.): ")

        try:
            nivel = normalizar_nivel(nivel_input)
        except ValueError as e:
            print(f"{e}")
            continue

        cuento = generar_cuento(tema, nivel)
        print("\n--- Cuento generado ---\n")
        print(cuento)

        ################
        #  AUDIO LOGIC #
        ################
        print("\n🎵 Generando audio... por favor espera")
        
        # Crear nombre de archivo para el audio
        from datetime import datetime
        import os
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        tema_limpio = "".join(c for c in tema if c.isalnum() or c in (' ', '-', '_')).rstrip()
        tema_limpio = tema_limpio.replace(' ', '_')[:20]
        nombre_archivo = f"audios_cuentos/{tema_limpio}_{nivel}_{timestamp}.mp3"
        
        # Crear directorio si no existe
        os.makedirs("audios_cuentos", exist_ok=True)
        
        audio_path = audio_gen.generar_audio(cuento, nombre_archivo)
        
        if audio_path:
            print(f"Audio listo para escuchar: {audio_path}")
        else:
            print("No se pudo generar el audio")

        ################
        # IMAGE LOGIC  #
        ################
        while True:
            descripcion = input(
                "\nDescribe una escena del cuento para generar la imagen: "
            )
            if not descripcion or len(descripcion.strip()) < 10:
                print(
                    "La descripción debe tener al menos 10 caracteres y no estar vacía. Intenta nuevamente."
                )
                continue
            break
        
        imagen_path = generar_imagen(descripcion, cuento, nivel)
        
        if imagen_path:
            print(f"Imagen generada: {imagen_path}")
        else:
            print("No se pudo generar la imagen")

if __name__ == "__main__":
    main()