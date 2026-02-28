install:
	pip install -r requirements.txt
format:
	black *.py
lint:
	pylint --disable=R,C,W0718,E1121 *.py
test:
	pytest test_*.py
run:
	python wikibot.py
all: install format lint test run