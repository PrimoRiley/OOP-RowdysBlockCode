run:
	python main.py

check_types:
	mypy --disallow-untyped-defs --strict button.py
	mypy --disallow-untyped-defs --strict block.py
	mypy --disallow-untyped-defs --strict food.py
	mypy --disallow-untyped-defs --strict rowdy.py

test:
	coverage run -m unittest discover -s unittesting