# Take_break

This a commandline application that helps you to take a break

## Prerequisites

- [python3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation/)
- [python3-dev](https://www.google.com/search?ei=-nxIXbaZCJG4gwf5xbsQ&q=python3-dev+installation&oq=python3-dev+installation&gs_l=psy-ab.3..0i22i30l6.31084.33914..35069...0.0..0.324.1505.2-3j2......0....1..gws-wiz.......0i71j35i304i39j0i13j0i13i5i30j0i8i13i30.OCLw3x0GXkM&ved=0ahUKEwi2_v6ntezjAhUR3OAKHfniDgIQ4dUDCAo&uact=5)
- [cup of coffee](https://www.wikihow.com/Make-Instant-Coffee)

## Installation

follow the instruction carefully

1. `git clone the repo` and into Take_break
2. create a virtual environment by running `virtualenv -p python3-dev venv`
3. initialize the env by running `source venv/bin/activate`
4. install the dependencies `pip install -r requirements.txt`
5. bundle the cli-app by running `python setup.py bdist_wheel --universal`
6. the pip install break-app `pip install dist/BreakApp-0.10-py2.py3-none-any.whl`
7. then run the app `breakapp`
