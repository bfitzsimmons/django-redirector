import os
from setuptools import setup, find_packages

doc_dir = os.path.join(os.path.dirname(__file__), 'docs')
index_filename = os.path.join(doc_dir, 'index.rst')
long_description = open(index_filename).read().split('split here', 1)[1]
version = '0.1.0'

setup(
    name = "django-redirector",
    version = version,
    packages = find_packages(),
    include_package_data=True,
    author = "Brant Fitzsimmons",
    author_email = "brant.fitzsimmons@gmail.com",
    license = 'BSD',
    description = "Redirect on 404s.",
    long_description = long_description,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
