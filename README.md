>> Generador de Cuentos Infantiles:
Este es un programa de consola que utiliza la API de OpenAI para generar cuentos infantiles personalizados. A partir de un tema y un nivel escolar ingresado por el usuario. El programa crea un cuento, genera una imagen y produce un archivo de audio con la narración del cuento.

>> Características_
- Generación de Cuentos: Crea historias originales para niños de 1° a 4° básico.
- Generación de Imágenes: Produce una imagen basada en una descripción de una escena del cuento.
- Generación de Audio: Convierte el texto del cuento en un archivo de audio MP3 para ser escuchado.

>> Requisitos Previos:
Para ejecutar este programa, necesitarás tener Python 3 instalado. Además, deberás instalar las siguientes librerías:
- openai: Para interactuar con la API de OpenAI.
- python-dotenv: Para gestionar las variables de entorno (como tu API key).

>> Configuración:
1. Crea un entorno vitual.
2. debes contar con una clave de API de OpenAI.
3. Archivo .env:
   - En la misma carpeta donde se encuentran los archivos del proyecto, crea un nuevo archivo llamado .env.
   - Dentro de este archivo, agrega la siguiente línea, reemplazando TU_API_KEY_AQUI con tu clave de API real:
		OPENAI_API_KEY="TU_API_KEY_AQUI"

>> Uso del Programa:
1. Abre una terminal o línea de comandos.
2. Navega hasta el directorio donde guardaste los archivos del proyecto.
3. Ejecuta el script principal con el siguiente comando:
   
	src/main.py
   
   También puedes ejecutar haciendo click en el ícono de la parte superior, en caso que uses VSC.

4. Sigue las instrucciones que aparecerán en la consola:
   - Primero, te pedirá el tema del cuento, en donde debe dar una breve descripción.
   - Luego, te solicitará el nivel escolar (puedes usar números como 1, 2, o texto como "primero básico").
   - Finalmente, después de generar el cuento y el audio, te pedirá que describas una escena para crear la imagen.


>>Archivos del Proyecto:
   - main.py: Es el punto inicial del programa y ordena la ejecución de los módulos.
   - cuento_generator.py: Contiene las instrucciones para generar el texto del cuento.
   - imagen_generator.py: Crear la imagen a partir de la descripción.
   - audio_generator.py: Convierte el texto del cuento en un archivo de audio.
   - openai_client.py: Gestiona la conexión y configuración del cliente de OpenAI.
   - utils.py: Incluye funciones de ayuda, como la que normaliza el nivel escolar.

>>Archivos Generados de salida:
Se crearán los siguientes archivos en el directorio del proyecto:
   - cuento_audio.mp3: El archivo de audio con la narración del cuento.
   - Una carpeta llamada imagenes_generadas/: Dentro de esta carpeta se guardará la imagen creada para el cuento.