# Proyecto-Aplicaciones-WWW

Proyecto Final Asignatura Aplicaciones en la WEB y Redes Inalámbricas

# Requerimientos

Python 3.11.0
postgresql .
git

# Instalacion

Pasos para realizar desde la consola cuando se tengan todos los requerimientos

1. descarga el repositorio usando git clone
2. crear un entorno virtual .venv
3. activamos el entorno virtual
4. instalamos los requerimientos del proyecto los cuales estan en _requirementes.txt_ esto lo hacemos ejecutando _pip install -r requirements.txt_ estando en la carpeta del proyecto
5. ejecutar el comando _python manage.py makemigrations_ y luego _python manage.py migrate_
6. finalmente _python manage.py runserver_ para lanzar el servidor de Django en el puerto indicado en la consola
