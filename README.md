# Advent of Code Solutions

This repo contains my solutions for [Advent of Code](https://adventofcode.com/).

You can copy the scripts to yourself and use it.

## Installation (Optional)

Create a virtualenv:

> Note:
> This is optional but to make `flake8` and `black` work, it needs to be done.
> If you installed those globally then there is no need for this.

```sh
python -m venv venv
venv/bin/pip install --upgrade pip
venv/bin/pip install -r requirements.txt
```

## Usage

### Create new day

```sh
./aoc.py -c <year> <day>
```

Example:

```sh
./aoc.py -c 2023 1
```

### Run the solution file

```sh
./aoc.py -r <year> <day>
```

Example:

```sh
./aoc.py -r 2023 1
```
