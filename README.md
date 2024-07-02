# Python-Django-PostgreSQL-Cancha

Aplicación web para la gestión y alquiler de canchas deportivas. La aplicación permite a los usuarios buscar, reservar y valorar canchas, así como gestionar sus propias reservas y perfiles. Además, proporciona funcionalidades administrativas para gestionar usuarios, canchas, reservas y comentarios.

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [API Endpoints](#api-endpoints)

## Instalación

### Prerrequisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:

- Python (versión 3.12.2)
- PostgreSQL (versión 16)
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

6. **Crea los roles por defecto:**

```bash
python manage.py create_default_rol
```

7. **Crea los estados de reservacion por defecto:**

```bash
python manager.py create_default_status_reservation
```

8. **Ejecutar el servidor:**

```bash
python manage.py runserver
```

¡Listo! El proyecto ahora debería estar en funcionamiento en tu entorno local. Puedes acceder a él desde tu navegador web visitando `http://localhost:8000`.

## Uso

1. Ejecuta el servidor de desarrollo: 

```
python manage.py runserver
```

2. Accede a la API a través de las URL definidas.

## API Endpoints

### Crear nuevo usuario

```http
POST /api/auth/signUp
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `full_name` | `string` | **Requerido**. Nombre completo del usuario |
| `email` | `string` | **Requerido**. Correo electrónico del usuario |
| `password` | `string` | **Requerido**. Contraseña del usuario |
| `phone` | `string` | **Requerido**. Numero celular del usuario |
| `birth_date` | `string` | **Requerido**. Fecha de nacimiento del usuario |
| `rol` | `int` | **Requerido**. Rol del usuario|

#### Registro de un nuevo usuario

```http
POST /api/auth/signUp
Content-Type: application/json

{
	"full_name": "test fullname",
	"email": "test@email.com",
	"password": "testpassword",
	"phone": "+57 321 987 6543",
	"birth_date": "1999-09-09",
	"rol": 2
}
```

#### Respuesta exitosa al registro

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
	"status": "success",
	"message": "Successful registration",
	"data": {
		"token": {
			"token_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
		},
		"user": {
			"id": 1,
			"full_name": "test fullname",
			"email": "test@email.com",
			"phone": "+57 321 987 6543",
			"birth_date": "1999-09-09",
			"is_active": true,
			"is_staff": false,
			"is_superuser": false,
			"rol": 2
		}
	}
}
```

### Inciar sesión de usuario

```http
POST /api/auth/signIn
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Requerido**. Email del usuario |
| `password` | `string` | **Requerido**. Contraseña del usuario |

#### Inicio de sesión de un usuario

```http
POST /api/auth/signIn
Content-Type: application/json

{
	"email": "test@email.com",
	"password": "testpassword"
}
```

#### Respuesta exitosa al inicio de sesión

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
	"status": "succes",
	"message": "Successful login",
	"data": {
		"token": {
			"token_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
			"token_expiration": "2024-06-10T02:27:34.039747Z"
		},
		"user": {
			"id": 1,
			"full_name": "test fullname",
			"email": "test@email.com",
			"phone": "+57 321 987 6543",
			"birth_date": "1999-09-09",
			"is_active": true,
			"is_staff": false,
			"is_superuser": false,
			"rol": 2
		}
	}
}
```

### Cerrar sesión de usuario

```http
GET /api/auth/signOut
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |

#### Cierre de sesión de un usuario

```http
GET /api/auth/signOut
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### Respuesta exitosa al cierre de sesión

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
	"status": "success",
	"message": "Successful logout"
}
```

### Actualizar al usuario

```http
POST /api/users/update
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `full_name` | `string` | Nombre completo del usuario |
| `email` | `string` | Correo electrónico del usuario |
| `password` | `string` | Contraseña del usuario |
| `phone` | `string` | Numero celular del usuario |
| `birth_date` | `string` | Fecha de nacimiento del usuario |
| `rol` | `int` | Rol del usuario|

#### Actualiza datos de un usuario

```http
POST /api/users/update
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

{
	"full_name": "test new fullname",
	"email": "testnew@email.com",
	"password": "testnewpassword",
	"phone": "+57 321 987 6543",
	"birth_date": "1999-09-09",
	"rol": 2
}
```

#### Respuesta exitosa al actualizar usuario

```http
HTTP/1.1 200 Ok
Content-Type: application/json

{
	"status": "success",
	"message": "Successful update",
	"data": {
		"token": {
			"token_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
			"token_expiration": "2024-06-10T20:37:44.026227Z"
		},
		"user": {
			"id": 1,
			"full_name": "test new fullname",
			"email": "testnew@email.com",
			"phone": "+57 320 476 9010",
			"birth_date": "1999-09-09",
			"is_active": true,
			"is_staff": false,
			"is_superuser": false,
			"rol": 2
		}
	}
}
```

### Eliminar un usuario

```http
DELETE /api/users/delete
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |

#### Elimina a un usuario

```http
DELETE /api/users/delete
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### Respuesta exitosa al eliminar usuario

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
	"status": "success",
	"message": "successful deleted"
}
```

### Buscar todos los usuarios como administrador

```http
GET /api/users/search
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |

#### Busca todos los usuarios como administrador

```http
GET /api/users/search
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### Respuesta exitosa al buscar todos los usuarios como administrador

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
	"status": "success",
	"message": "All users retrieved successfully",
	"data": {
		"result": 2,
		"user": [
			{
				"id": 1,
				"full_name": "test fullname1",
				"email": "test1@email.com",
				"phone": "+57 320 476 9010",
				"birth_date": "1999-09-09",
				"is_active": true,
				"is_staff": false,
				"is_superuser": false,
				"rol": 2
			},
			{
				"id": 2,
				"full_name": "Test fullname2",
				"email": "test2@email.com",
				"phone": "+57 323 542 2103",
				"birth_date": "1999-09-09",
				"is_active": true,
				"is_staff": false,
				"is_superuser": false,
				"rol": 2
			}
		]
	}
}
```

### Buscar usuarios con párametro como administrador

```http
GET /api/users/search?query=
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |
| `query`     |	`string`   |	**Requerido**. Consulta de búsqueda |

**tipos de busquedas:**
- Nombre completo del usuario
- Email del usuario
- Numero celular del usuario
- Rol del usuario
- Estado del usuario

#### Busca usuarios con parámetro como administrador

```http
GET /api/users/search?query=consulta_de_búsqueda
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### Respuesta exitosa al buscar usuarios como administrador

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
	"status": "success",
	"message": "User found successfully",
	"data": {
		"result": 2,
		"user": [
			{
				"id": 1,
				"full_name": "test fullname1",
				"email": "test1@email.com",
				"phone": "+57 320 476 9010",
				"birth_date": "1999-09-09",
				"is_active": true,
				"is_staff": false,
				"is_superuser": false,
				"rol": 2
			},
			{
				"id": 2,
				"full_name": "Test fullname2",
				"email": "test2@email.com",
				"phone": "+57 323 542 2103",
				"birth_date": "1999-09-09",
				"is_active": true,
				"is_staff": false,
				"is_superuser": false,
				"rol": 2
			}
		]
	}
}
```

### Activar/Desactivar usuarios como administrador

```http
PATCH /api/users/change-status/{user_id}
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |
| `user_id` | `int` | **Requerido**. ID del usuario |
| `action`     |	`string`   |	**Requerido**. Acción a realizar: "activate" para activar al usuario o "deactivate" para desactivarlo. |

#### Activa usuario como administrador

```http
PATCH /api/users/change-status/{user_id}
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

{
	"action": "activate"
}
```

#### Respuesta exitosa al activar el usuario como administrador

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
	"status": "success",
	"message": "User activated successfully"
}
```

#### Desactiva usuario como administrador

```http
PATCH /api/users/change-status/{user_id}
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

{
	"action": "deactivate"
}
```

#### Respuesta exitosa al desactivar el usuario como administrador

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
	"status": "success",
	"message": "User deactivated successfully"
}
```

### Cambiar el rol a un usuario como administrador

```http
PATCH /api/users/change-role/{user_id}
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |
| `user_id` | `int` | **Requerido**. ID del usuario |
| `action`     |	`string`   |	**Requerido**. Acción a realizar: "user" para usuario o "admin" para administrador |

#### Cambia el rol a user como administrador

```http
PATCH /api/users/change-role/{user_id}
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

{
	"action": "user"
}
```

#### Respuesta exitosa a cambiar el rol a user como administrador

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
	"status": "success",
	"message": "successful role change",
	"data": {
		"token": {
			"token_key": "693774e3f7a7be669b12fa95c454f6c466c90d3e",
			"token_expiration": "2024-06-11T18:43:04.359593Z"
		},
		"user": {
			"id": 1,
			"full_name": "test fullname1",
			"email": "test1@email.com",
			"phone": "+57 320 476 9010",
			"birth_date": "1999-09-09",
			"is_active": true,
			"is_staff": false,
			"is_superuser": false,
			"rol": 2
		}
	}
}
```

#### Cambia el rol a admin como administrador

```http
PATCH /api/users/change-role/{user_id}
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

{
	"action": "admin"
}
```

#### Respuesta exitosa a cambiar el rol a admin como administrador

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
	"status": "success",
	"message": "successful role change",
	"data": {
		"token": {
			"token_key": "693774e3f7a7be669b12fa95c454f6c466c90d3e",
			"token_expiration": "2024-06-11T18:43:04.359593Z"
		},
		"user": {
			"id": 1,
			"full_name": "test fullname1",
			"email": "test1@email.com",
			"phone": "+57 320 476 9010",
			"birth_date": "1999-09-09",
			"is_active": true,
			"is_staff": true,
			"is_superuser": true,
			"rol": 1
		}
	}
}
```

### Eliminar a un usuario como administrador

```http
DELETE /api/users/delete-user/{user_id}
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |
| `user_id` | `int` | **Requerido**. ID del usuario |

#### Elimina a un usuario como administrador

```http
DELETE /api/users/delete-user/{user_id}
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### Respuesta exitosa a eliminar un usuario como administrador

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
	"status": "success",
	"message": "user deleted successfully"
}
```

### Crear tipos de superficies de canchas por administrador

```http
POST /api/courts/surface-types
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |
| `type` | `string` | **Requerido**. Tipo de superficie|

#### Crea un tipo de superficie de cancha por administrador

```http
POST /api/courts/surface-types
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

{
	"type": "Grass court"
}
```

#### Respuesta exitosa a crear un tipo de superficie de cancha por administrador

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
	"status": "success",
	"message": "Successfully created surface type",
	"data": {
		"surface_type": {
			"id": 1,
			"type": "Grass court"
		}
	}
}
```

### Obtener tipos de superficies de canchas por administrador

```http
GET /api/courts/surface-types
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |

#### Obtiene los tipos de superficies de canchas por administrador

```http
GET /api/courts/surface-types
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### Respuesta exitosa a obtener los tipos de superficies de canchas por administrador
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
	"status": "success",
	"message": "Correctly obtained surface types",
	"data": {
		"surface_type": [
			{
				"id": 1,
				"type": "Grass court"
			},
			{
				"id": 2,
				"type": "Synthetic court"
			}
		]
	}
}
```

### Crear estados de canchas por administrador

```http
POST /api/courts/court-status
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |
| `status` | `string` | **Requerido**. Estado de cancha|

#### Crea un estado de cancha por administrador

```http
POST /api/courts/court-status
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

{
	"status": "Available"
}
```

#### Respuesta exitosa a crear un estado de cancha por administrador

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
	"status": "success",
	"message": "Successfully created surface type",
	"data": {
		"court_status": {
			"id": 1,
			"status": "Available"
		}
	}
}
```

### Obtener estados de canchas por administrador

```http
GET /api/courts/court-status
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |

#### Obtiene los estados de canchas por administrador

```http
GET /api/courts/court-status
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### Respuesta exitosa a obtener los estados de canchas por administrador
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
	"status": "success",
	"message": "Correctly obtained court status",
	"data": {
		"court_status": [
			{
				"id": 1,
				"status": "Available"
			},
			{
				"id": 2,
				"status": "Reserved"
			}
		]
	}
}
```

### Crear tipos de canchas por administrador

```http
POST /api/courts/surface-types
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |
| `type` | `string` | **Requerido**. Tipo de cacnha|

#### Crea un tipo de cancha por administrador

```http
POST /api/courts/court-types
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

{
	"type": "Basketball court"
}
```

#### Respuesta exitosa a crear un tipo de cancha por administrador

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
	"status": "success",
	"message": "Successfully created court type",
	"data": {
		"court_type": {
			"id": 1,
			"type": "Basketball court"
		}
	}
}
```

### Obtener tipos de superficies de canchas por administrador

```http
GET /api/courts/court-types
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |

#### Obtiene los tipos de superficies de canchas por administrador

```http
GET /api/courts/court-types
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### Respuesta exitosa a obtener los tipos de superficies de canchas por administrador
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
	"status": "success",
	"message": "Correctly obtained court types",
	"data": {
		"surface_type": [
			{
				"id": 1,
				"type": "Basketball court"
			},
			{
				"id": 2,
				"type": "Volleyball court"
			}
		]
	}
}
```

### Crear una cancha por administrador

```http
POST /api/courts/add-court
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |
| `name` | `string` | **Requerido**. Nombre de la cancha|
| `code` | `string` | **Requerido**. Código de la cancha|
| `size` | `string` | **Requerido**. Tamaño de la cancha|
| `location` | `string` | **Requerido**. Ubicación de la cancha|
| `price_hour` | `decimal` | **Requerido**. Precio por hora de la cancha|
| `description` | `string` | Descripcion de la cancha |
| `cover_image` | `string` | Imagen de portada de la cancha |
| `surface_type` | `int` | **Requerido**. ID del tipo de superficie|
| `court_status` | `int` | **Requerido**. ID del estado de cancha|
| `court_type` | `int` | **Requerido**. ID del tipo de cancha|

#### Crea una cancha por administrador

```http
POST /api/courts/add-court
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

{
  "name": "Central Court",
  "code": "CC001",
  "size": "20x40",
  "location": "Main Ave 123, Sports City",
  "price_hour": 150.00,
  "description": "A modern court with LED lighting and locker rooms.",
  "cover_image": "uploads/central_court.jpg",
  "surface_type": 1,
  "court_status": 1,
  "court_type": 1
}
```

#### Respuesta exitosa a crear una cancha por administrador

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
	"status": "success",
	"message": "Court created correctly",
	"data": {
		"court": {
			"id": 1,
			"name": "Central Court",
			"code": "CC001",
			"size": "20x40",
			"location": "Main Ave 123, Sports City",
			"price_hour": "150.00",
			"description": "A modern court with LED lighting and locker rooms.",
			"cover_image": "uploads/central_court.jpg",
			"surface_type": 1,
			"court_status": 1,
			"court_type": 1
		}
	}
}
```

### Actualizar una cancha por administrador

```http
PUT /api/courts/update-court/{court_id}
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |
| `court_id` | `int` | **Requerido**. ID de la cancha |
| `name` | `string` | Nombre de la cancha|
| `code` | `string` | Código de la cancha|
| `size` | `string` | Tamaño de la cancha|
| `location` | `string` | Ubicación de la cancha|
| `price_hour` | `decimal` | Precio por hora de la cancha|
| `description` | `string` | Descripcion de la cancha |
| `cover_image` | `file` | Imagen de portada de la cancha |
| `surface_type` | `int` | ID del tipo de superficie|
| `court_status` | `int` | ID del estado de cancha|
| `court_type` | `int` | ID del tipo de cancha|

#### Actualiza una cancha por administrador

```http
PUT /api/courts/update-court/{court_id}
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

{
  "name": "New Central Court",
  "code": "CC011",
  "size": "20x45",
  "location": "New Main Ave 123, Sports City",
  "price_hour": 155.00,
  "description": "A modern court with LED lighting and locker rooms.",
  "cover_image": "uploads/central_court.jpg",
  "surface_type": 1,
  "court_status": 1,
  "court_type": 1
}
```

#### Respuesta exitosa a actualizar una cancha por administrador

```http
HTTP/1.1 200 Ok
Content-Type: application/json

{
	"status": "success",
	"message": "Court updated correctly",
	"data": {
		"court": {
			"id": 1,
			"name": "New Central Court",
			"code": "CC011",
			"size": "20x45",
			"location": "New Main Ave 123, Sports City",
			"price_hour": "155.00",
			"description": "A modern court with LED lighting and locker rooms.",
			"cover_image": "uploads/central_court.jpg",
			"surface_type": 1,
			"court_status": 1,
			"court_type": 1
		}
	}
}
```

### Eliminar una cancha por administrador

```http
DELETE /api/courts/delete-court/{court_id}
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |
| `court_id` | `int` | **Requerido**. ID de la cancha |

#### Elimina una cancha por administrador

```http
DELETE /api/courts/delete-court/{court_id}
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### Respuesta exitosa a eliminar una cancha por administrador

```http
HTTP/1.1 200 Ok
Content-Type: application/json

{
	"status": "success",
	"message": "Court deleted successfully"
}
```

### Agregar imagenes de las canchas por administrador

```http
POST /api/courts/add-court-image
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |
| `image` | `file` | **Requerido**. Imagen de la cancha |
| `court` | `int` | **Requerido**. ID de la cancha |

#### Agrega imagenes de la cancha por administrador

```http
POST /api/courts/add-court-image
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

{
	"image": "uploads/central_court_1.jpg",
	"court": 1
}
```

#### Respuesta exitosa a agregar imagen de la cancha por administrador

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
	"status": "success",
	"message": "Court image added successfully",
	"data": {
		"image_court": {
			"id": 1,
			"image": "/uploads/central_court_1.jpg",
			"court": 1
		}
	}
}
```

### Obtener imagenes de la cancha por administrador

```http
GET /api/courts/get-court-image/{court_id}
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |
| `court_id` | `int` | **Requerido**. ID de la cancha |

#### Obtiene imagenes de la cancha por administrador

```http
GET /api/courts/get-court-image/{court_id}
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### Respuesta exitosa a obtener imagenes de la cancha por administrador

```http
HTTP/1.1 200 Ok
Content-Type: application/json

{
	"status": "success",
	"message": "Court images geted successfully",
	"data": [
		{
			"id": 1,
			"image": "/uploads/central_court_1.jpg",
			"court": 1
		},
		{
			"id": 2,
			"image": "/uploads/central_court_2.jpg",
			"court": 1
		}
	]
}
```

### Eliminar imagen de las canchas por administrador

```http
DELETE /api/courts/delete-court-image/{court_id}
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |
| `court_id` | `int` | **Requerido**. ID de la cancha |

#### Elimina imagenes de la cancha por administrador

```http
DELETE /api/courts/delete-court-image/{court_id}
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### Respuesta exitosa a eliminar imagen de la cancha por administrador

```http
HTTP/1.1 200 Ok
Content-Type: application/json

{
	"status": "success",
	"message": "Court images deleted successfully"
}
```

### Buscar todas las canchas

```http
GET /api/courts/search-court
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |

#### Busca todas las canchas

```http
GET /api/courts/search-court
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### Respuesta exitosa al buscar todas las canchas

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
	"status": "success",
	"message": "Curts correctly obtained",
	"data": {
		"result": 8,
		"courts": [
			{
				"id": 1,
				"name": "Emerald Field",
				"code": "CX501",
				"size": "20x40",
				"location": "1234 Evergreen Avenue, Springfield, Illinois",
				"price_hour": "100.00",
				"description": "Emerald Field is a premier sports facility located in Springfield, Illinois.",
				"cover_image": "uploads/test_image_3.jpg",
				"surface_type": 1,
				"court_status": 1,
				"court_type": 1
			},
			{
				"id": 1,
				"name": "Sunset Courts",
				"code": "CZ201",
				"size": "20x40",
				"location": "456 Sunset Boulevard, Los Angeles, California",
				"price_hour": "120.00",
				"description": "Sunset Courts offers state-of-the-art facilities for tennis and basketball enthusiasts.",
				"cover_image": "uploads/test_image_4.jpg",
				"surface_type": 1,
				"court_status": 1,
				"court_type": 1
			}
		],
		"court_images": [
			{
				"id": 1,
				"image": "/uploads/test_image_1.jpg",
				"court": 1
			},
			{
				"id": 2,
				"image": "/uploads/test_image_2.jpg",
				"court": 1
			},
			{
				"id": 3,
				"image": "/uploads/test_image_3.jpg",
				"court": 2
			}
		]
	}
}
```

### Buscar canchas con parámetros

```http
GET /api/courts/search-court?query=
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |
| `query`     |	`string`   |	**Requerido**. Consulta de búsqueda |

**tipos de busquedas:**
- Nombre de la cancha
- Código de la cancha
- Tamaño de la cancha
- Ubicación de la cancha
- Precio por hora de la cancha
- Descripción de la cancha
- Tipo de superficie de la cancha
- Estado de la cancha de la cancha
- Tipo de cancha de la cancha

#### Busca canchas con parámetros

```http
GET /api/courts/search-court?query=consulta_de_búsqueda
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### Respuesta exitosa al buscar canchas con parámetro

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
	"status": "success",
	"message": "Curts correctly obtained",
	"data": {
		"result": 8,
		"courts": [
			{
				"id": 1,
				"name": "Emerald Field",
				"code": "CX501",
				"size": "20x40",
				"location": "1234 Evergreen Avenue, Springfield, Illinois",
				"price_hour": "100.00",
				"description": "Emerald Field is a premier sports facility located in Springfield, Illinois.",
				"cover_image": "uploads/test_image_3.jpg",
				"surface_type": 1,
				"court_status": 1,
				"court_type": 1
			},
			{
				"id": 1,
				"name": "Sunset Courts",
				"code": "CZ201",
				"size": "20x40",
				"location": "456 Sunset Boulevard, Los Angeles, California",
				"price_hour": "120.00",
				"description": "Sunset Courts offers state-of-the-art facilities for tennis and basketball enthusiasts.",
				"cover_image": "uploads/test_image_4.jpg",
				"surface_type": 1,
				"court_status": 1,
				"court_type": 1
			}
		],
		"court_images": [
			{
				"id": 1,
				"image": "/uploads/test_image_1.jpg",
				"court": 1
			},
			{
				"id": 2,
				"image": "/uploads/test_image_2.jpg",
				"court": 1
			},
			{
				"id": 3,
				"image": "/uploads/test_image_3.jpg",
				"court": 2
			}
		]
	}
}
```

### Crear una reservacion de una cancha

```http
POST /api/reserves/reserve-court
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |
| `start_datatime` | `datetime` | **Requerido**. Fecha de inicio de la reservacion |
| `end_datatime` | `datetime` | **Requerido**. Fecha de fin de la reservacion |
| `status` | `int` | **Requerido**. ID del estado de reservacion |
| `user` | `int` | **Requerido**. ID del usuario |
| `court` | `int` | **Requerido**. ID de la cancha |

#### Crea una reservacion de una cancha

```http
POST /api/reserves/reserve-court
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

{
	"start_datetime": "2024-07-01T15:30",
	"end_datetime": "2024-07-01T16:30",
	"status": 1,
	"user": 1,
	"court": 1
}
```

#### Respuesta exitosa a reservar una cancha

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
	"status": "success",
	"message": "Reservation created successfully",
	"data": {
		"id": 1,
		"start_datetime": "2024-07-01T15:30",
		"end_datetime": "2024-07-01T16:30",
		"status": 1,
		"user": 1,
		"court": 1
	}
}
```

### Obtener las reservaciones de un usuario

```http
GET /api/reserves/user-reservations
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |
| `page` | `int` | Numero de la pagina |

#### Obtiene las reservaciones de un usuario

```
GET /api/reserves/user-reservations
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### Obtiene las reservaciones de un usuario paginada

```http
GET /api/reserves/user-reservations?page={numero_de_la_pagina}
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### Respuesta exitosa al obtener las reservaciones de un usuario

```http
HTTP/1.1 200 Ok
Content-Type: application/json

{
	"status": "success",
	"message": "Reservations obtained correctly",
	"data": {
		"reservations": [
			{
				"id": 1,
				"start_datetime": "2024-06-27T14:30:00Z",
				"end_datetime": "2024-06-27T16:30:00Z",
				"status": 1,
				"user": 1,
				"court": 1
			},
			{
				"id": 2,
				"start_datetime": "2024-06-27T14:30:00Z",
				"end_datetime": "2024-06-27T16:30:00Z",
				"status": 1,
				"user": 1,
				"court": 2
			}
		]
	}
}
```

### Obtener todas las reservaciones por admin

```http
GET /api/reserves/reservations
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |
| `page` | `int` | Numero de la pagina |

#### Obtiene todas las reservaciones por admin

```
GET /api/reserves/reservations
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### Obtiene todas las reservaciones paginada por admin

```http
GET /api/reserves/reservations?page={numero_de_la_pagina}
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### Respuesta exitosa al obtener todas las reservaciones por admin

```http
HTTP/1.1 200 Ok
Content-Type: application/json

{
	"status": "success",
	"message": "Reservations obtained correctly",
	"data": {
		"reservations": [
			{
				"id": 1,
				"start_datetime": "2024-06-27T14:30:00Z",
				"end_datetime": "2024-06-27T16:30:00Z",
				"status": 1,
				"user": 1,
				"court": 1
			},
			{
				"id": 2,
				"start_datetime": "2024-06-27T14:30:00Z",
				"end_datetime": "2024-06-27T16:30:00Z",
				"status": 1,
				"user": 1,
				"court": 2
			},
			{
				"id": 3,
				"start_datetime": "2024-06-27T14:30:00Z",
				"end_datetime": "2024-06-27T16:30:00Z",
				"status": 1,
				"user": 2,
				"court": 3
			}
		]
	}
}
```