from setuptools import setup

setup(
    name='pyPandasRelationalDB',
    version='0.1.0',
    description='A singleton class for connecting to various databases using SQLAlchemy and returning pandas dataframes',
    author='Andres Manrique',
    author_email='andress0199@outlook.com',
    packages=['pyPandasRelationalDB'],
    install_requires=['pandas', 'sqlalchemy']
)