.PHONY: install test clean build

install:
	pip install -r requirements.txt
	pip install -e .

test:
	pytest tests/

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +

build:
	python setup.py bdist_wheel

all: clean install test build

