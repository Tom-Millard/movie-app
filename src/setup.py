import os

from setuptools import setup

setup(
    name='movie-app',
    version='0.0.0',
    description='',
    author='Tom Millard',
    packages=['main', 'movie'],
    include_package_data=True,
    install_requires=[
        'Flask',
        'click',
        'requests',
        'bs4',
        'python-dotenv',
        'pycodestyle',
        'autopep8'
    ],
)
