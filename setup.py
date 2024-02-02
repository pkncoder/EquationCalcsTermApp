from setuptools import setup

setup(
    name='solve',
    version='1.0.0',
    py_modules=['solve'],
    install_requires=[
        'click'
    ],
    entry_points={
        'console_scripts': [
            'solve = solve:cli',
        ],
    },
)