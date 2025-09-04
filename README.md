Generador de Cuentos Infantiles

Este proyecto es una aplicación de consola que utiliza la API de OpenAI para generar cuentos infantiles personalizados.
A partir de un tema y un nivel escolar ingresado por el usuario, el programa genera:

•	Un cuento en formato texto.

•	Una narración en audio (MP3).

•	Una ilustración asociada al cuento.

•	Un archivo PDF que combina texto e imagen.

Está diseñado para estudiantes de 1° a 4° básico.

Características

•	Generación de Cuentos: historias originales adaptadas según el nivel educativo.

•	Narración en Audio: el cuento se convierte automáticamente a un archivo MP3.

•	Generación de Imágenes: ilustraciones en estilo infantil basadas en el tema del cuento.

•	PDF Integrado: se genera un documento en PDF que incluye la historia y su ilustración.

•	Organización de Archivos: cada cuento se guarda en una carpeta única con sus archivos de salida.

Requisitos

•	Python 3.10+

•	Una clave de API de OpenAI -> válida.

Dependencias de Python (listadas en requirements.txt):

openai
python-dotenv
requests
reportlab

Instalación

1.	Clona este repositorio:

git clone https://github.com/tu_usuario/generador-cuentos.git
cd generador-cuentos

2.	Crea un entorno virtual:

python -m venv venv

3.	Activa el entorno virtual:

•	En Windows (PowerShell):

venv\Scripts\Activate.ps1

•	En Linux/MacOS:

source venv/bin/activate

4.	Instala las dependencias:

pip install -r requirements.txt

5.	Configura tu clave de API.
Crea un archivo .env en la raíz del proyecto con el siguiente contenido:

OPENAI_API_KEY="TU_API_KEY_AQUI"

Uso

Ejecuta el script principal desde la carpeta raíz del proyecto:

python src/main.py

El programa solicitará:

1)	Un tema para el cuento (ejemplo: Dinosaurios en el bosque).

2)	El nivel escolar (ejemplo: 1, 2, primero, segundo básico, etc.).

3)	Automáticamente se generará el cuento en texto, narración en audio, imagen y PDF.

Archivos de Salida

Los resultados se guardan dentro de la carpeta outputs/, en una subcarpeta única por cuento, con los siguientes archivos:

•	cuento.txt → cuento en texto plano.

•	cuento.mp3 → narración en audio.

•	cuento.jpg → ilustración generada.

•	cuento.pdf → documento PDF con texto e imagen integrados.

Ejemplo

Entrada:

Tema del cuento: Dinosaurios en la escuela
Nivel escolar: segundo básico

Salida esperada:

•	Un cuento adaptado a nivel 2° básico.

•	Archivo de audio cuento.mp3.

•	Imagen cuento.jpg.

•	PDF cuento.pdf con la historia ilustrada.

Licencia

Este proyecto está bajo la licencia MIT.
Puedes usarlo, modificarlo y distribuirlo libremente.
