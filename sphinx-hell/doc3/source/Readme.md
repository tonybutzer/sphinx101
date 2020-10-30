# README Sphinx

## Student Exercise
https://github.com/repository-preservation/lcmap-merlin/tree/develop/docs/source/api

## Hacked link

http://10.12.68.246:8443/autoapi/vegetLib/vegetLib/index.html

## Goal

- to get the api documented using sphinx

- talk about reStructured Text

## admin stuff
add ssh keys from jupyter-kagone on this host to github skagone - delete old key


## Installation

```

cd pkg
make

```

## Configure

- do this again so steffi and gabe see how it is done and what it creates
    - source
    - build
    - Makefile

```
make -f makefile* run

vi source/index.rst

make html
```

## Customize

2. add markdown capabilities
    - copy this readme or symlink - copy is probably easier
1. add auto api

- do this live

## Comments

### I was wrong sphinx is not really simple! - tony

### What I like about Sphinx

- search
- can use markdown
- easy to run from source to build/html
- consistent with the professional ReadTheDocs


### What I don't like about Sphinx

- lots of knobs
- likely overkill for small projects
	- time investment
- needs a web http server to be really usefull

### Alternatives

- pydoc
- help(func)

