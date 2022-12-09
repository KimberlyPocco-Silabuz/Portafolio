# PROYECTO UNIDAD 04 PORTAFOLIO
_Kimberly Pocco Pariona_

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

Mira **Instalación** para conocer como desplegar el proyecto.
## Comenzando 🚀

### Pre-requisitos 📋

_Que cosas necesitas para instalar el software y como instalarlas_

### Instalación 🔧
_Primeramente deberá crear su entorno virtual para trabajar con estas librerías_
```
pip install django
```
```
pip install mysqlclient
```
Cambiar el nombre de la base de datos en  **DATABASES**  dentro de settings del proyecto para poder realizar las migraciones
```
python manage.py makemigrations blog
```
```
python manage.py migrate blog
```

* [Template](https://bootstrapmade.com/iportfolio-bootstrap-portfolio-websites-template/) - Este es el template Boostrap utilizado