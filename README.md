# Yummy-Recipes-Django-REST-API


## Product overview 
 Yummy-Recipes-Django-REST-API is a simple  API built with  Django and Django Rest Framework.  Enables you to register a user,login. It aslo provides CRUD functionality for categories and recipes assigned to these categories. 

## Development set up
- Check that python 3, pip, virtualenv and postgres are installed

- Clone  Yummy-Recipes-Django-REST-API  repo and cd into it
    ```
    git clone https://github.com/owenbob/Yummy-Recipes-Django-REST-API.git
    ```
- Create virtual env
    ```
    virtualenv --python=python3 venv
    ```
- Activate virtual env
    ```
    source venv/bin/activate
    ```
- Install dependencies
    ```
    pip install -r requirements.txt
    ```
- Create Application environment variables and save them in .env file
    ```
    export DBNAME='Your Database name'
    export DBPASSWORD='Your Database password'
    export DBUSER='Your Database user'
    ```
- Run command
    ```
    source .env
    ```
- Running migrations

     ```
     python manage.py migrate 
    ```
- Run application.
    ```
    cd YummyRecipes/
    ```
    ```
    python manage.py runserver
    ```
- Run Tests
    ```
    cd YummyRecipes/
    ```
    ```
    coverage run  --source='.' manage.py test
    ```

## Built with 
- Python version  3
- Django
- Django Rest Framework
- Postgres