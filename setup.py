from setuptools import find_packages, setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, './README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='UserInputParser',
    packages=find_packages(),
    version='v0.1.0',
    license='MIT',
    description='Parse user input to ensure it meets the specified constraints',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jake Kalish',
    author_email='jkalish14@gmail.com',
    url='https://github.com/jkalish14/UserInputParser',
    keywords=['Parser', 'User', 'Input'],  # Keywords
)
