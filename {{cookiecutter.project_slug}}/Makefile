.PHONY: clean clean-build clean-pyc clean-test coverage dist help \
        lint lint/flake8 lint/pylint pytype deploy local_deploy reqs \
        help_venv

.DEFAULT_GOAL := help

PROJECT={{ cookiecutter.project_slug }}

PYTEST_TARGET = ${PROJECT}
PYTEST_EXTRA_FLAGS = 
PYTEST_MINCOV = --cov-fail-under=60
PYTEST_COV = --cov=${PYTEST_TARGET} --cov-report term-missing ${PYTEST_MINCOV}
PYTEST_FLAGS = -vvv --doctest-modules --doctest-glob='*.md' \
               --maxfail=20


################################################################
#                                                              #
#  PYTEST_IGNORE gets added to for stuff tester should ignore. #
#  Note that we need := for assignment to keep appending       #

PYTEST_IGONRE = 

# Ignore setup.py
PYTEST_IGNORE := ${PYTEST_IGNORE} --ignore=setup.py

# Ignore venv
PYTEST_IGNORE := ${PYTEST_IGNORE} --ignore=venv_${PROJECT} --ignore=venv

# End PYTEST_IGNORE section                                    #
#                                                              #
################################################################


define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

help_venv:  ## Show help on how to setup virtual environment
	@echo "Do \"python3 -m venv venv_${PROJECT}\" to setup venv"
	@echo "Then do \"source venv_${PROJECT}/bin/activate\" to use it."

deploy:  ## deploy running docker containers onto this machine
	${MAKE} -C docker deploy
local_deploy:  ## deploy running docker containers with "local" ports
	${MAKE} -C docker local_deploy
docker_down:  ## bring down docker containers created from this project
	${MAKE} -C docker docker_down

reqs:  ## Make requirements by install things via pip
	@if [ -z "`which pip | grep venv`" ] ; then \
		echo "Does not seem like you setup venv; try make help_venv" &&\
			exit 1 ; fi
	pip install -r requirements_dev.txt

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint/flake8: ## quick check of style with flake8
	flake8 ${PROJECT} tests

lint/pylint: ## check style with pylint
	pylint ${PROJECT} tests \
             --jobs=4

lint: lint/flake8 lint/pylint

pytype:
	pytype ${PROJECT}

# Note that we set pipefail on the command since `tee` always returns status 0
# so we need pipefail if we want this command to fail on test failure.
test: ## Run our regression tests
	set -o pipefail && \
          py.test ${PYTEST_FLAGS} ${PYTEST_IGNORE} \
            ${PYTEST_EXTRA_FLAGS} ${PYTEST_TARGET} 2>&1 | tee ./test_log.txt

check: ## Run all our checks including linting, type-checking, tests, etc.
	${MAKE} lint
	${MAKE} pytype
	${MAKE} test

coverage: ## check code coverage quickly with the default Python
	coverage run --source ${PROJECT} -m pytest
	coverage report -m
	coverage html

