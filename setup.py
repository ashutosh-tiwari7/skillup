from setuptools import setup

setup(
    name = 'main',
    version = '1',
    description = 'Automatic parking system',
    author = 'Ashutosh Tiwari',
    url = '',
    license = 'MIT',
    packages = ['main'],
    entry_points = {'console_scripts': ['skillup = main.main',],},
)