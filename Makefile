init:
	pip install -r requirements.txt

setup:
	echo "Activating Python environment: source venv/bin/activate"
	source venv/bin/activate

test:
	echo "Start executing: python mouse_bot.py --time=.1"	
	python mouse_bot.py --time=.1
	echo "Done executing: python mouse_bot.py --time=.1"

.PHONY: init setup test

