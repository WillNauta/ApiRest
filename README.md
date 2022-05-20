# ApiRest
# ApiRest

# Use Api Spotify

![by @Willia](https://github.com/WilliamQuinteroT/ApiRest/myapp1.PNG "Use the api Spotify---Api")


# Información
Lo primero que hacemos es importar los módulos o librerías que vamos a necesitar; en este caso pandas y spotipy:


Funciones Disponibles
- Connect to api.

# Instalar 🛠️
- - - - - - - - - - - - - - - - - - - - - - - - -
-Install this pack
```
Necesitamos los modulos de spotipy y pandas. Si nos los tenemos, los instalaremos escribiendo en la consola:
    pip install spotipy
    pip install pandas
```

# Pasos para correr la api 🚀
- - - - - - - - - - - - - - - - - - - - - - - - -

- A continuación y gracias a la librería spotipy, nos conectaremos a Spotify con nuestras claves Client ID y Client Secret.

Ahora ya nos queda acceder a nuestra playlist para descargarnos la lista de canciones que la conforman. ¿Pero cómo lo hacemos? Necesitamos el identificador de la playlist que podemos obtener fácilmente de la aplicación oficial. Sólo tenemos que acceder al menú de opciones de la playlist y seleccionar la opción «Compartir > Copiar URI de Spotify». Lo que obtenemos es la siguiente cadena spotify:user:***usuario***:playlist:***codigoplaylist*** con el nombre de tu usuario y el código de la playlist. Así que copia el nombre del usuario y el código de la playlist, y pégalos en la siguiente línea de python:

Ahora para cada canción sólo faltaría realizar las llamadas pertinentes y obtener la información que queremos para acabar exportando todo a una serie de ficheros. Sencillo, ¿no?

A continuación dejo el código fuente de este pequeño programa para que lo descargues si quieres. Recuerda que no está optimizado ni es muy limpio; el objetivo era didáctico y sin querer perder mucho el tiempo… Aunque al final estoy utilizándolo para #OneDayOneSong.
```
Para hacer una divisison, lo que hacemos es pasar dos parametros
http://127.0.0.1:5000//calcula-sisdis?tipo=division&valor1=2&valor2=3
```
Lo primero que hacemos es importar los módulos o librerías que vamos a necesitar; en este caso pandas y spotipy:


""" Necesitamos los modulos de spotipy y pandas. Si nos los tenemos, los instalaremos escribiendo en la consola:
    pip install spotipy
    pip install pandas
"""


A continuación y gracias a la librería spotipy, nos conectaremos a Spotify con nuestras claves Client ID y Client Secret.

Ahora ya nos queda acceder a nuestra playlist para descargarnos la lista de canciones que la conforman. ¿Pero cómo lo hacemos? Necesitamos el identificador de la playlist que podemos obtener fácilmente de la aplicación oficial. Sólo tenemos que acceder al menú de opciones de la playlist y seleccionar la opción «Compartir > Copiar URI de Spotify». Lo que obtenemos es la siguiente cadena spotify:user:***usuario***:playlist:***codigoplaylist*** con el nombre de tu usuario y el código de la playlist. Así que copia el nombre del usuario y el código de la playlist, y pégalos en la siguiente línea de python:


Ahora para cada canción sólo faltaría realizar las llamadas pertinentes y obtener la información que queremos para acabar exportando todo a una serie de ficheros. Sencillo, ¿no?

A continuación dejo el código fuente de este pequeño programa para que lo descargues si quieres. Recuerda que no está optimizado ni es muy limpio; el objetivo era didáctico y sin querer perder mucho el tiempo… Aunque al final estoy utilizándolo para #OneDayOneSong.