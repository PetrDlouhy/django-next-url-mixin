=============================
Django next url mixin
=============================

.. image:: https://badge.fury.io/py/django-next-url-mixin.svg
    :target: https://badge.fury.io/py/django-next-url-mixin

.. image:: https://travis-ci.org/PetrDlouhy/django-next-url-mixin.svg?branch=master
    :target: https://travis-ci.org/PetrDlouhy/django-next-url-mixin

.. image:: https://codecov.io/gh/PetrDlouhy/django-next-url-mixin/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/PetrDlouhy/django-next-url-mixin

Next url mixin which is safe to phishing attacks

Naive implementation of the next URL mechanism is vulnerable to phishing attacks.
This implementation aims to

1) raise awareness of that
2) provide safe implementation (possibly seen by more eyes)

The mixin does it's work in form_valid() function, so it can be used for offspring of FormView or simillar view classes.

Documentation
-------------

The full documentation is at https://django-next-url-mixin.readthedocs.io.

Quickstart
----------

Install Django next url mixin::

    pip install django-next-url-mixin

Use it in your views:

.. code-block:: python

    from django.views.generic.edit import FormView
    from next_url_mixin.mixin import NextUrlMixin

    class MyView(NextUrlMixin, FormView):

        # If you are overriding form_valid(), don't forgot to return the super value with the redirect to the new url
        def form_valid(self, *args, **kwargs):
            return_value = super().form_valid(*args, **kwargs)
            return return_value
      


Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
