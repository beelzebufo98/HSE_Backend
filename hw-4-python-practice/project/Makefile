PIP := venv\Scripts\pip
PYTHON3 := venv\Scripts\python
TEST := venv\Scripts\pytest -v utils/test_controllers.py
clear:
	rmdir /S /Q venv

venv:
	python -m venv venv

requirements:
	${PIP} install -r requirements.txt

run:
	${PYTHON3} utils/server.py

setup:
	make clear
	make venv
	make requirements

test:
	${TEST}
