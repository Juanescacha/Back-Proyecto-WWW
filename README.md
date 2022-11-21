# Proyecto Aplicaciones-WEB

Proyecto Final Asignatura Aplicaciones en la WEB y Redes Inalámbricas

Miguel Ángel Rincón Clavijo - 1942985
Carlos Bermudez Valencia - 1927623
Juan Esteban Camargo Chacón - 1924984

### _Requerimientos_

Python 3.11.0
postgresql .
git

### _Instalacion_

Pasos para realizar desde la consola cuando se tengan todos los requerimientos

- Descarga el repositorio usando **git clone**
- crear un entorno virtual **.venv** y activalo
- Instala los requerimientos del proyecto los cuales estan en **requirements.txt** esto lo hacemos ejecutando:
  `pip install -r requirements.txt` estando en la carpeta del proyecto
- ejecutar el comando `python manage.py makemigrations` y luego `python manage.py migrate`
- finalmente `python manage.py runserver` para lanzar el servidor de Django en el puerto indicado en la consola
