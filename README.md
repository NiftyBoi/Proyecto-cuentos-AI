📚 Generador de Cuentos Infantiles

Este es un programa de consola que utiliza la API de OpenAI para generar cuentos infantiles personalizados. A partir de un tema y un nivel escolar ingresado por el usuario, el programa:

✍️ Crea un cuento original.

🖼️ Genera una imagen relacionada con una escena del cuento.

🔊 Produce un archivo de audio narrando la historia.

Está diseñado para niños de 1° a 4° básico.

🚀 Características

Generación de Cuentos → Historias adaptadas según nivel escolar.

Generación de Imágenes → Escenas ilustradas basadas en descripciones del cuento.

Generación de Audio → Conversión de texto a narración en formato MP3.

📦 Requisitos

Antes de comenzar, asegúrate de tener instalado:

Python 3.10+

Librerías necesarias (ver más abajo).

Una API Key de OpenAI válida.

⚙️ Instalación y Configuración

Clona este repositorio

git clone https://github.com/tu_usuario/generador-cuentos.git
cd generador-cuentos


Crea un entorno virtual

python -m venv venv


Activa el entorno virtual

En Windows:

venv\Scripts\activate


En Linux/MacOS:

source venv/bin/activate


Instala dependencias

pip install -r requirements.txt


Configura tu clave de API

Crea un archivo .env en la raíz del proyecto con el siguiente contenido:

OPENAI_API_KEY="TU_API_KEY_AQUI"

▶️ Uso del Programa

Ejecuta el script principal:

python src/main.py


El programa te guiará paso a paso:

Ingresa un tema para el cuento (ejemplo: "animales en el bosque").

Escribe el nivel escolar (ejemplo: 1, 2, o segundo básico).

Una vez generado el cuento y el audio, describe una escena para crear la ilustración.

📂 Estructura del Proyecto
📦 generador-cuentos
├── 📂 src
│   ├── main.py                # Punto inicial del programa
│   ├── cuento_generator.py     # Generación del texto del cuento
│   ├── imagen_generator.py     # Creación de imágenes
│   ├── audio_generator.py      # Narración en audio (MP3)
│   ├── openai_client.py        # Configuración del cliente OpenAI
│   └── utils.py                # Funciones auxiliares
├── .env                        # Clave API de OpenAI (no subir a GitHub)
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Documentación

📤 Archivos de Salida

cuento_audio.mp3 → narración del cuento.

imagenes_generadas/ → carpeta con las imágenes creadas.

✅ Ejemplo
>> Tema del cuento: Dinosaurios amigables en la escuela
>> Nivel escolar: 2
>> Escena para ilustrar: Un dinosaurio enseñando matemáticas a los niños


Salida esperada:

Un cuento adaptado al nivel 2° básico.

Archivo de audio cuento_audio.mp3.

Imagen generada en imagenes_generadas/.

🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si quieres mejorar este proyecto:

Haz un fork.

Crea una rama con tu mejora: git checkout -b mi-mejora.

Haz commit de los cambios: git commit -m "Agrega nueva funcionalidad".

Haz push a la rama: git push origin mi-mejora.

Abre un Pull Request.

📜 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo y modificarlo libremente.