# Backend for vuejs-app

## Tools used

- as database Postgresql9.5
- in backend Python3.x + Django2.x
- in testing and dev sqlite3
- Django rest framework
- Graphene-Django and GraphQL

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
### Accounts

* `POST /accounts/token-auth/`  
    in the body section ```{'username_or_email: '', 'password':''}```
    - login user and get token
* `POST /accounts/token-verify/`  
    in the body section ```{'token': ''}```
    - verify token
* `POST /accounts/token-refresh/`  
    in the body section ```{'token': ''}```
    - refresh old token        
* `POST /accounts/signup/`  
    in the body section ```{'username': '', 'email': '', 'password': '', 'first_name': '', 'last_name': '', 'birth_date': '', 'photo':''}```
    - create new user    
* `POST /accounts/update/`
    - update user
    - in body section - any user information
* `GET /accounts/profile/`
    - get info about authenticated user
* `GET /accounts/user_profile/[id]`
    - get info about user by id
* `POST /accounts/logout/` 
    - logout user

Password reset [Link](https://github.com/anx-ckreuzberger/django-rest-passwordreset)

* `POST /accounts/password-reset/`
    - restore password with sending email
    - in the body section ```{'email': email@email.com}```
* `POST /accounts/password-reset/confirm/`
    - reset password 
    - in the body section ```{'password': password, 'token': token}```
    
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
* `graphql`
    - shows QraphQL tool for building queries   

##Extra info
* YYYY-MM-DD - date format

* YYYY-MM-DD HH:MM:SS - date_time format

* In every query(except login and signup, contacts page), in header use
```{
'content-type':'application/json',
'authentication': 'Bearer [token]',
}```