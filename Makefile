#!/usr/bin/make
#

.PHONY: setup
setup:  ## Setups environment
	virtualenv .
	./bin/pip install --upgrade pip
	./bin/pip install -r requirements.txt
	./bin/pip install --no-deps .

.PHONY: test
test:  ## Runs test
	. ./bin/activate && python -m unittest discover tests

.PHONY: cleanall
cleanall:  ## Cleans all installed files
	rm -fr bin include lib local share

