from setuptools import setup
 
setup(
    name='el',
    version='0.1.0',
    install_requires=[
        'click == 8.1.7',
    ],
    entry_points={
        'console_scripts': [
            'el = el:main',
        ]
    }
)