from setuptools import setup

setup(
    name='lametric',
    version='2.0.0',
    description='Lametric API wrapper written on Python. ',
    url='https://github.com/breitburg/python-lametric',
    author='Ilya Breitburg',
    author_email='me@breitburg.com',
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
    install_requires=['requests', 'upnpclient', 'munch'],
    project_urls={
        'Bug Reports': 'https://github.com/breitburg/python-lametric/issues',
        'Source': 'https://github.com/breitburg/python-lametric',
    },
)
