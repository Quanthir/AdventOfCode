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

Creates 3 files in the `<year>/<day>` folder.

- `challenge.txt`: Copy/Paste the puzzle text parts in this file to easy access.
- `input.txt`: The input text that is given to you for that day.
- `solution.py`: The Python file to solve the puzzle. Automatically reads the `input.txt` file.


### Run the solution file

```sh
./aoc.py -r <year> <day>
```

Example:

```sh
./aoc.py -r 2023 1
```
