# Api-de-Pagos
_Api de pagos usando Django._

## Comenzando🚀

_Primero hay que iniciar y clonar el repositorio._
```
git init
git clone #link-del-repositorio
```
### Instalación

_Ahora que tenemos la repo en nuestro VisualStudio hay que crear venv y activarlo._

```
py -m venv .\venv  //crear el env
venv\Scripts.\activate //activarlo
```
_detallito , si no tienes los permisos de windows usar el siguiente 'comando' antes de activarlo._

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process  //comando
```

### Requerimientos

_Toca instalar los requerimientos del venv._

```
pip install -r requirements.txt
```

### Migraciones

_Ya esta casi todo para empezar , solo falta hacerlas tablas. Para eso hay que hacer las migraciones._

```
py manage.py makemigrations
```

_y luego._

```
py manage.py migrate
```

### Los links del api

_para poder ver la api hay varios links._
```
http://localhost:8000/users/signup/    ---> para registrarte
http://localhost:8000/users/login/---> para logearte
http://localhost:8000/users/servis/servicio/ --->para los servicios
http://localhost:8000/users/pagis/pago/  --->para los pagos
```

_Y eso es todo._


