# Python-Django-PostgreSQL-Cancha

Aplicación web para la gestión y alquiler de canchas deportivas. La aplicación permite a los usuarios buscar, reservar y valorar canchas, así como gestionar sus propias reservas y perfiles. Además, proporciona funcionalidades administrativas para gestionar usuarios, canchas, reservas y comentarios.

## Tabla de Contenidos

- [Instalación](#instalación)

## Instalación

### Prerrequisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:

- Python (versión 3.12.2)
- PostgreSQK (versión 16)
- pip (administrador de paquetes de Python)

### Pasos de Instalación

1. **Clona este repositorio:**

```bash
git clone https://github.com/JohannGaviria/Python-Django-PostgreSQL-Cancha.git
```

2. **Crear el entorno virtual:**

Utiliza `virtualenv` o otro gestor de entornos virtuales

```bash
pip install virtualenv
python -m virtualenv nombre_del_entorno
```

3. **Instalar las dependencias:**

```bash
cd Python-Django-PostgreSQL-Cancha
pip install -r requirements.txt
```

4. **Configurar la base de datos:**

- Crea una base de datos PostgreSQL en tu entorno.
- Crea un archivo `.env` en la ruta raiz de tu proyecto y crea las variables de entorno con los datos correpodientes:
    - SECRET_KEY=tu_clave_secreta
    - ENGINE=tu_base_de_datos
    - NAME=tu_nombre_de_la_base_de_datos
    - USER=tu_usuario_de_la_base_de_datos
    - PASSWORD=tu_contraseña_de_la_base_de_datos
    - HOST=tu_host
    - PORT=tu_port

5. **Crea las migraciones:**

```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Ejecutar el servidor:**

```bash
python manage.py runserver
```

¡Listo! El proyecto ahora debería estar en funcionamiento en tu entorno local. Puedes acceder a él desde tu navegador web visitando `http://localhost:8000`.
