.DEFAULT_GOAL := build

build-and-upload: build upload

build:
	rm -rf src/dist/*.tar.gz*
	cd src && python setup.py sdist

upload:
	twine upload src/dist/*.tar.gz
