from setuptools import setup

setup(
    name='uhh',
    version='0.1.0',
    packages=['uhh'],
    entry_points={
        'console_scripts': [
            'uhh = uhh.__main__:main'
        ]
    })
