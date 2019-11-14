# blog
 Créeation d'application réutilisable

- requirement : setuptools

## Empaquetage de l’application
 1. créez un répertoire parent pour myblog, en dehors de votre projet Django. Nommez ce répertoire django-nan-myblog
 2. Déplacez le répertoire myblog dans le répertoire django-nan-myblog.
 3. Créez un fichier django-nan-myblog/README.rst contenant ceci :
  ```
  =====
myblog
=====

myblog is a simple Django app to build blog.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'myblog',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('myblog/', include('myblog.urls')),

3. Run `python manage.py migrate` to create the myblog models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/myblog/
  ```
  4. Créez un fichier django-nan-myblog/LICENSE
  5. Next we’ll create setup.cfg and setup.py files which detail how to build and install the app. A full explanation of these files is beyond the scope of this tutorial, but the setuptools documentation has a good explanation. Create the files django-nan-myblog/setup.cfg and django-nan-myblog/setup.py with the following contents:

