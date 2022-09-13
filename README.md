# EasyArchive

My command line utility that I created for backing up folders to another computer. I created
this as a way to learn python.

# Usage

Coming soon. The project at this time is still a work in progress so a command line usage hasn't been established yet.

# Development workflow

I used pyenv and pyenv-virtualenv for this project. PipEnv maybe be a better option overall though.

* git clone to local workstation
* create a virtual environment

```shell
pyenv local 3.10.6
pyenv virtualenv easyarchive3106
pyenv local easyarchive3106
```

* install dependencies and upgrade python friends

```shell
python3 -m pip install --upgrade pip setuptools wheel
```

* install local project module

```shell
pip install -e src/
```
