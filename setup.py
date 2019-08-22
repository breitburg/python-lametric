from setuptools import setup

setup(
    name='lametric',
    version='2.0',
    description='Library for controlling LaMetric Time using official device API ',
    url='https://github.com/breitburg/python-lametric',
    author='breitburg',
    author_email='contact@breitburg.me',
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
    install_requires=['requests', 'upnpclient'],
    project_urls={
        'Bug Reports': 'https://github.com/breitburg/python-lametric/issues',
        'Source': 'https://github.com/breitburg/python-lametric',
    },
)
