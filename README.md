# Existenciality
Existenciality is a Django based web application that shows general questions about life. Check out the [web application](djangoimilla.herokuapp.com) on Heroku

## How it was built
Following the main instructions from the [official documentation](https://docs.djangoproject.com/en/3.1/intro/tutorial01/) on Django!

## Built Setup
If you want to run the code of this project you can follow these instructions:

1. Clone this respository

```
git clone https://github.com/luucamay/existenciality.git
```
2. [Download and install Python 3](https://www.python.org/downloads/)

3. Set up a virtual environment first. For windows with git bash:

```
source ~/.virtualenvs/djangodev/Scripts/activate
```

4. Use pip to install Django
```
 python -m pip install Django
```

5. Verify your django installation. Open the python interactive shell and execute the next lines of code.

```
>>> import django
>>> print(django.get_version())
3.1
```

6. Setup database
* Create the required tables defined at settings.py in the INSTALLEDD_APPS array. Make the migration happen

```
python manage.py migrate
```

* Create the admin user
```
python manage.py createsuperuser
```

7. Open the admin view: http://127.0.0.1:8000/admin
8. Create questions in the admin view
9. Open the app view: http://127.0.0.1:8000

## Articulo sobre esta aplicacion
Si te interesa o quieres saber como construir esta aplicacion puedes leer esta [guia](https://www.djangoproject.com/start/)
