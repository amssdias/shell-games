[python-download]: https://www.python.org/downloads/
[docker-link]: https://docs.docker.com/get-docker/

![Python Badge](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Workflow branch master](https://github.com/amssdias/shell-games/actions/workflows/testing.yml/badge.svg?branch=master)
[![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://https://docker.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


<h1 align=center>Shell Games</h1>

My project is a program that brings the classic games of Hangman and Battleship to the computer terminal. Users can choose to play either game and enjoy the challenge of guessing the hidden word or sinking their opponent's ships. The program is easy to use and provides an entertaining way to pass the time and exercise your brain. With intuitive controls and engaging gameplay, our program is sure to be a hit with users of all ages.


## :hammer: Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Pre requisites

- [Python][python-download] - 3.9
- [Docker](https://www.docker.com/) (Optional)

### Installing


1. Clone this repository to your local machine
2. Navigate to the project directory


```
git clone https://github.com/amssdias/shell-games.git
cd shell-games
```

#### With Docker

1. Build the Docker image:

```
docker build -t shell_games .
```

2. Run the Docker container:

```
docker run -it shell_games
```

#### Without Docker


1. Install requirements with pip:

```python
pip install -r requirements.txt
```

2. Run program:

```python
python base.py
```


## :mag_right: Usage

Just follow the instructions on the terminal.

<img src="img/usage.gif" alt="your gif">

Have fun :smile:
