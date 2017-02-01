help:	## Show this help.
		@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

freeze:	## Freeze currently installed packages into requirements.txt
	pip freeze > requirements.txt

init:	## Install requirements
	pip install -r requirements.txt

setup:	## Deprecated
	echo "Activating Python environment: source venv/bin/activate"
	source venv/bin/activate

# source command doesn't work with make. Ensure we chmod 755 venv/bin/activate first
test:	## Test with a mouse movement for 0.1 minute
	echo "Start executing: python mouse_bot.py --time=.1"
	. venv/bin/activate
	python mouse_bot.py --time=.1
	echo "Done executing: python mouse_bot.py --time=.1"

.PHONY: init setup test

