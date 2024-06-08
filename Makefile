install:
	pip install -r requirements.txt

lint:
	pylint core.py

test:
	pytest -vv