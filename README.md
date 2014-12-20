# buspointServer-getting-started


Esta app esta basada en en django para python.

Esta aplicacion soporta el articulo[Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) - check it out.

## Ejecutar Localmente

Asegurarse de Tener Python [instalado correctamente](http://install.python-guide.org).  Tambien instalar [Heroku Toolbelt](https://toolbelt.heroku.com/).

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started
$ pip install -r requirements.txt
$ python manage.py syncdb
$ foreman start web
```

La aplicacino debe de ejecutarse en [localhost:5000](http://localhost:5000/).

## Desarrollo en Heroku

```sh
$ heroku create
$ git push heroku master
$ heroku run python manage.py syncdb
$ heroku open
```

## Documentacion
Para mas informacion sobre python en Heroku, vea:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)

