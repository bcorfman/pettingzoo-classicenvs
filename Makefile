PACKAGE := pettingzoo-tictactoe
PACKAGE_DIR := src/${PACKAGE}
SHELL := env PYTHON_VERSION=3.12 /bin/bash
.SILENT: run devinstall install test lint format
PYTHON_VERSION ?= 3.12

setup:
	curl -sSf https://rye-up.com/get | RYE_NO_AUTO_INSTALL=1 RYE_INSTALL_OPTION="--yes" bash

install:
	$(HOME)/.rye/shims/rye sync --no-dev

devinstall:
	$(HOME)/.rye/shims/rye pin $(PYTHON_VERSION)
	$(HOME)/.rye/shims/rye add ipython pytest pytest-cov --dev
	$(HOME)/.rye/shims/rye sync

run: 
	$(HOME)/.rye/shims/rye run python main.py

lint:
	$(HOME)/.rye/shims/rye lint -q -- --select I --fix 

format:
	$(HOME)/.rye/shims/rye fmt

all: devinstall lint format test
