# Introduccion

Este es el Proyecto Final de la asignatura Aplicaciones en la WEB y Redes Inalámbricas

Integrantes:

- Miguel Ángel Rincón Clavijo - 1942985
- Carlos Bermudez Valencia - 1927623
- Daniel Felipe Vélez Cuaical - 1924306
- Juan Esteban Camargo Chacón - 1924984
- Alejandro Satizabal Narvaez - 1726041

### _Requerimientos_

- Python3
- Pipenv
- postgresql

### _Instalacion_

- Clonar el proyecto a tu maquina local `git clone https://github.com/Juanescacha/Proyecto-Aplicaciones-WWW`
- Activa el entorno virtual de python `pipenv shell`
- Instala los requerimientos del proyecto los cuales estan en **Pipfile** esto lo hacemos ejecutando: `pipenv install`
- Navega a la carpeta **frontend/** `cd frontend/` y ejecuta `npm install` para instalar las dependencias
- Navega a la carpeta **backend/** ejecutar el comando `python manage.py makemigrations` y luego `python manage.py migrate`

### _Ejecutar la Aplicacion_

Vas a necesitar dos terminales, una para el frontend y otra para el backend para iniciar los servidores de esta aplicacion.

1. Ejecuta este comando para inciar el servidor de backend desde la carpeta **backend/** `python manage.py runserver` (recuerda ejecutar este comando teniendo activo el entorno virtual)

2. Ejecuta este comando para iniciar el servidor del frontend de desarrollo desde la carpeta **frontend/** `npm start` (esto iniciara el frontend en [localhost:3000](localhost:3000))

### _Construido con_

- [Django](https://www.djangoproject.com/) - un framework de desarrollo web de alto nivel escrito en Python que fomenta el desarrollo rápido y un diseño limpio y pragmático.

- [React](https://es.reactjs.org/) - una biblioteca JavaScript de código abierto con fines de desarrollo de interfaces de usuario en el front-end.

- [Python](https://www.python.org/) - un lenguaje de programación interpretado cuya filosofía hace hincapié en una sintaxis que favorezca un código legible.

- [Postgresql](https://www.postgresql.org/) - un sistema de gestión de bases de datos objeto relacional (ORDBMS) de código abierto.


- Descarga el repositorio usando `git clone`
- crear un entorno virtual **.venv** y activalo
- Instala los requerimientos del proyecto los cuales estan en **requirements.txt** esto lo hacemos ejecutando:
  `pip install -r requirements.txt` estando en la carpeta del proyecto
- Exportar las variables de entorno para la conexión con la base de datos:
  - En GNU/Linux:
    `source export_env_vars.sh`
- ejecutar el comando `python manage.py makemigrations` y luego `python manage.py migrate`
- finalmente `python manage.py runserver` para lanzar el servidor de Django en el puerto indicado en la consola
