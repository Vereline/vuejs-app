# vuejs-app

Test app in vuejs

1. folder frontend - vuejs + graphql
2. folder backend - django + graphql + postgresql (sqlite in testing and dev) 
3. folder services - flask (as service)
4. folder playground - nodejs - express (as service)
5. folder docker_container - all things above make as separate docker images in containers and make a config/run/start-stop script

# Frontend
TODO

# Backend

## Tools used

- as database Postgresql9.5
- in backend Python3.x + Django2.x
- in testing sqlite3
- in frontend Vuejs
- Django rest framework

## Installation

1. ```python3 -m venv venv```
2. ```source venv/bin/activate```
3. ```pip install -r requirements.txt```
4. ```mkdir vuejs_app/logs```
5. ```touch vuejs_app/logs/main_debug.log vuejs_app/logs/main.log```

## Setting up environment

1. Create .env file
2. Fill it with appropriate data

    * DATABASE_URL=postgres://[username]:[password]@0.0.0.0:5432/[db_name]
    * DEBUG=[True/False]
    * BASE_URL=http://[host]:[port]
    * PORT=[port]
    * HOSTNAME=[host]
    * SECRET_KEY=[secret_key]

## Creating Django Admin User
1. ```python manage.py createsuperuser```

## Running
1. ``` python manage.py migrate```
2. ``` python manage.py runserver```
3. Custom port ``` python manage.py runserver [port number]```
4. ``` python manage.py runserver 0.0.0.0:8000```

## Testing
### Run all the tests 
```$ ./manage.py test```

### Run all the tests in the [folder].tests module
```$ ./manage.py test [folder].tests```

### Run all the tests found within the '[package]' package
```$ ./manage.py test [package]```

### Run just one test case
```$ ./manage.py test [folder].[test_*.py file].[*TestCase]```

### Run just one test method
```$ ./manage.py test [folder].[test_*.py file].[*TestCase].[test_*]```


## API reference

### Miscellaneous
Run in the browser

* `api-docs/`
    - shows all api requests as Swagger auto-generated documentation
* `api-auth/login/`
    - login for DRF Browsable API
* `api-auth/logout/`
    - logout for DRF Browsable API
* `admin/`
    - shows admin page
* `static/`
    - shows static files of application
* `media/`
    - shows media files of application
* `docs/`
    - shows default drf documentation
* `schema/`
    - shows schema of application    

##Extra info
* YYYY-MM-DD - date format

* YYYY-MM-DD HH:MM:SS - date_time format

* In every query(except login and signup, contacts page), in header use
```{
'content-type':'application/json',
'authentication': 'Bearer [token]',
}```

# Services
TODO

# Playground
TODO
