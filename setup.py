#!usr/bin/python
from setuptools import setup, find_packages
setup(
    name='BreakApp',
    description='An application that gives you a break when run',
    version='0.10',
    packages=find_packages(),  # list of all packages
    install_requires=['inflect'],
    python_requires='>=2.7',  # any python greater than 3.6
    test_suite="tests",  # where to find tests
    entry_points={
        'console_scripts': [
                    'breakapp = take_break.__main__:main',
            # 'app2 = app2.__main__:main'
        ]
    }
)
