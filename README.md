# Take_break

This a commandline application that helps you to take a break

## Prerequisites

- [python3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation/)
- [python3-dev](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-16-04-server)
- [cup of coffee](https://www.wikihow.com/Make-Instant-Coffee)

## Installation

follow the instruction carefully

1. `git clone the repo` and into Take_break
2. create a virtual environment by running `virtualenv -p python3 venv`
3. initialize the env by running `source venv/bin/activate`
4. install the dependencies `pip install -r requirements.txt`
5. bundle the cli-app by running `python3 setup.py bdist_wheel --universal`
6. the pip install break-app `pip install dist/BreakApp-0.10-py2.py3-none-any.whl`
7. then run the app `breakapp`

---------------------------------------------------------------------------------------
   
Build setup.py `python3 setup.py build`
Install setup.py dependencies `python3 setup.py install`

## python version 3.10 +

follow the instruction carefully


1. `git clone the repo` and into Take_break
2. create a virtual environment by running and initialize the env by running `pipenv shell`
3. install the dependencies `pipenv install`
4. bundle the cli-app by running `python3 setup.py bdist_wheel --universal`
5. the pip install break-app `pipenv install dist/BreakApp-0.10-py2.py3-none-any.whl`
6. run the app `breakapp`
   
   DEBUG ERROR
   Go to folder
   cd /usr/lib/python3.10/collections/__init__.py
   Edit
   --------------------------------------------------------------------
   try:
    from collections.abc import Mapping
   except ImportError:
    pass
   --------------------------------------------------------------------
   
7. run the app `breakapp`

---------------------------------------------------------------------------------------

Build setup.py `python3 -m build`
