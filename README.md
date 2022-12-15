[python-download]: https://www.python.org/downloads/
[docker-link]: https://docs.docker.com/get-docker/

![Python Badge](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Workflow branch master](https://github.com/amssdias/shell-games/actions/workflows/testing.yml/badge.svg?branch=master)
[![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://https://docker.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


<h1 align=center>Shell Games</h1>

Shell Games is a repository where there are many games produced in the shell. Some of this games I have already made when I started to code, but I decided to create a project with all of them using some design patterns.


## :hammer: Getting started

### Pre requisites

- [Python][python-download] - 3.9


### Installation

#### Clone the project

```
git clone https://github.com/amssdias/shell-games.git
cd shell-games
```


### :mag_right: Usage

[![Docker](https://i.imgur.com/VyjCJuz.png)](https://www.docker.com/)
<br>

Install [Docker][docker-link] here.

Once installed, open your terminal on the project folder and run:
```
docker build -t shell_games .
```

This will build an image, so you can run and play without configure anything.
To play all you need is run:
```
docker run -it shell_games
```

### Without docker

On a terminal window:
```python
pip install -r requirements.txt
python base.py
```

Have fun :smile:


## Design patterns used

- High Cohesion
- Low Coupling
- Strategy pattern
- Template method pattern
