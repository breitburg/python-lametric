from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'readme.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='python-lametric',
    version='1.0',
    description='Library for controlling LaMetric Time using official device API ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ketsu8/python-lametric',
    author='ketsu8',
    author_email='ilya.breytburg@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='lametric python',
    packages=['lametric'],
    install_requires=['requests'],
    project_urls={
        'Bug Reports': 'https://github.com/ketsu8/python-lametric/issues',
        'Source': 'https://github.com/ketsu8/python-lametric',
    },
)
