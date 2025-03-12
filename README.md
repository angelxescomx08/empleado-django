# Empleado Django

## Instalación

```bash
pip install -r requirements.txt
```

## Congelación de dependencias

```bash
pip freeze > requirements.txt
```

## Activación de virtual environment

Para linux
```bash
python -m venv env
source env/bin/activate
```
para windows
```bash
python -m venv env
env\Scripts\activate
```


## Ejecución

```bash
py manage.py runserver
```

## Despliegue

```bash
py manage.py makemigrations
py manage.py migrate
py manage.py collectstatic
py manage.py runserver
```
# Crear super usuario
```bash
py manage.py createsuperuser
```

# Levantar la base de datos
```bash
docker-compose up -d
```