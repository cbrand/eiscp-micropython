.DEFAULT_GOAL := build

build-and-upload: build upload

build:
	python setup.py sdist

upload:
	twine upload dist/*.tar.gz
