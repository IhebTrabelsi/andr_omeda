andr_omeda
==========

Integrating telegram bots with django ticketing system backend

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy andr_omeda

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Deployment
----------

The following details how to deploy this application.



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html



Custom Bootstrap Compilation
^^^^^^

The generated CSS is set up with automatic Bootstrap recompilation with variables of your choice.
Bootstrap v4 is installed using npm and customised by tweaking your variables in ``static/sass/custom_bootstrap_vars``.

You can find a list of available variables `in the bootstrap source`_, or get explanations on them in the `Bootstrap docs`_.



.. _in the bootstrap source: https://github.com/twbs/bootstrap/blob/v4-dev/scss/_variables.scss
.. _Bootstrap docs: https://getbootstrap.com/docs/4.1/getting-started/theming/

Scheduled Enhancements
----------

[ ] workspaces as "communities" in oku 
[ ] moderated_objects for each workspace ( with different types )


Current workflow
----------

Celery
^^^^^^^^^^^
Run celery (for windows):

::

  $ cmd>W:\andr_back\andr_omeda> celery -A andr_omeda worker -l info -P gevent (for windows)
  
Redis
^^^^^^^^^^^
Run redis server (for windows):

::

  $ wsl> redis-server
  
Django
^^^^^^^^^^^
Run Django server (for windows):

::

  $ cmd>W:\andr_back\andr_omeda> python manage.py runserver 127.0.0.1:8001
  
Postman
^^^^^^^^^^^
Create bot/bots for erp user:

::

  $ POST> http://127.0.0.1:8001/erp/bots/user123456/tokenjnejfkjegfzkjegeggzzgegz/
  body: 
    erp_owner_name: user123458
    token: 1732768364:AAF6rhx9U9Bmn6sGQAOPTNab_hmUQB8T8yg
    
Webhook + ngrok
^^^^^^^^^^^
Set webhook for new ngrok domain:

::

  $ cmd> python manage.py reset_webhook_for_ngrok 123456.ngrok.io 1732768364:AAF6rhx9U9Bmn6sGQAOPTNab_hmUQB8T8yg



