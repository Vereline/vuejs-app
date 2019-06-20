# Services for vuejs-app

## Tools used

- in backend Python3.x + Flask
- as database Postgresql9.5
- in testing and dev sqlite3

## Installation

1. ```python3 -m venv venv```
2. ```source venv/bin/activate```
3. ```pip install -r requirements.txt```

## Running application

1. ```cd vuejs_app```
2. ```export FLASK_APP=flaskr```
3. ```export FLASK_ENV=development```
4. ```flask init-db``` - to initialize database
5. ```flask run```

## Install project via setup.py

```pip install -e .```

## Testing 

 - Run ```pytest```
 - Tests coverage ```coverage run -m pytest```
 - Coverage report ```coverage report```
 - Coverage report in html ```coverage html```

## Build and Install on another machine 

1. ```python setup.py bdist_wheel```
2. ```export FLASK_APP=flaskr```
3. ```flask init-db```

## Run on production

1. ``` waitress-serve --call 'flaskr:create_app' ```
