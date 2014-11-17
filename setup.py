from setuptools import setup, find_packages


requires = []

setup(
    name='dicks-api',
    version='0.1',
    description='dicks-api (http://dicks-api.herokuapp.com/) library',
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
    ],
    author='andrzej3393',
    author_email='andrzej3393@gmail.com',
    packages=find_packages(),
    install_requires=requires,
)
