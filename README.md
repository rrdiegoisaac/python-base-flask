# BASE DE APLICACION FLASK

## INSTALACION

### ENTORNO VIRTUAL 
Instalar entorno virtual:

```
python -m pip install virtualenv
```

### CREAR ENTORNO VIRTUAL 

```
python -m venv venv
```


### ACTIVAR ENTORNO VIRTUAL

```
source venv/scripts/activate
```

### INSTALAMOS LAS DEPENDENCIAS NECESARIAS

```
pip install -r requirements.txt
```

### CREAR ARCHIVO .ENV

```
FLASK_ENV=dev
JWT_SECRET_KEY=
JWT_ACCESS_TOKEN_EXPIRES_HOURS=
JWT_ACCESS_TOKEN_EXPIRES_DAYS=
SECRET_KEY=
```


## EJECUTAR 
```
flask run --host=0.0.0.0 --port=5151
```

### GESTION BASE DE DATOS

## INICIAR BASE DE DATOS
```
python manage.py db init
```

## TOMAR FOTOGRAFIA ACTUAL DE LA BASE DE DATOS
```
python manage.py db migrate
```

## CARGAR FOTOGRAFIA A LA BASE DE DATOS
```
python manage.py db upgrade
```