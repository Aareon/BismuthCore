# BismuthCore
[Alpha] Home of the BismuthCore Python Package


## BISMUTH

Bismuth is a Python Crypto currency, written from scratch.

It ambitions to be a simple yet effective blockchain and platform, with many innovative mechanisms under the hood and real world use cases.

Read more at http://Bismuth.cz

## BismuthCore

This python package contains all core classes needed by the Bismuth node.   
It's targeted toward clean and stable code, with tests and doc, rather than bleeding edge experiments.

## Install

`pip3 install BismuthCore`

## Development
```sh
py -m pip install pip -U  # Update pip
py -m pip install poetry  # Install poetry
poetry install  # Install project requirements & dev dependencies
poetry shell  # Activate virtual environment
ruff check  # Perform checks using ruff
pytest  # Run tests
```
Please run tests with `pytest` and `ruff check` before submitting any changes.

## Current state

Alpha - Do not use.

At the moment, it's mainly an architectural and design work to be used by core devs only.

