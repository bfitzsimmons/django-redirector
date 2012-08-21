django-redirector
=================

django-redirector provides a mechanism by which requests for URLs that result in a 404 response can be 301 redirected to
another location.

.. toctree::
   :maxdepth: 2
   :hidden:

   changelog

.. comment: split here

Installation
************

To install the latest release (currently 1.6.3) using pip::

    pip install django-exposure

To install the development version from github using pip::

    pip install -e git://github.com/natgeo/django-exposure.git

Add ``exposure`` to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'exposure',
        ...
    )

Usage
*****

Add the following to your project's settings.py file::

    EXPOSURE_MAX_HEIGHT = 4000
    EXPOSURE_MAX_WIDTH = 4000
    EXPOSURE_EXPIRE_SECS = 3600

Then access your files as you normally would through templates::

    <img src="{{ object.photo|resize:"WIDTH HEIGHT [CROP]" }}" alt="some image" />

For example, the following will yield a 200x200 version of your image, cropped::

    <img src="{{ object.photo|resize:"200 200 0" }}" alt="some image" />

You can also use an alternate syntax for resize dimensions::

    <img src="{{ object.photo|resize:"200x200 0" }}" alt="some image" />

The resize filter also accepts a URL::

    <img src="{{ object.photo.url|resize:"200x200 0" }}" alt="some image" />

Tests
*****

To run the tests, add ``exposure`` to your ``INSTALLED_APPS`` and run::

    django-admin.py test exposure

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

