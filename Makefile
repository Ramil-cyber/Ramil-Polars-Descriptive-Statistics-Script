setup:
	pip3 install -r requirements.txt

lint:
	pylint --exit-zero main.py

test:
	pytest

format:
	black main.py