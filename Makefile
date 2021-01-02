.DEFAULT_GOAL := build

build-and-upload: build upload

build:
	cd src && python setup.py sdist

upload:
	twine upload src/dist/*.tar.gz
