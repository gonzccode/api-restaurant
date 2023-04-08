# Restaurant Api
This is a project about an API for the management of a restaurant.

## Used technologies
1. Flask
2. PostgreSQL
3. SQLAlchemy
4. PyJWT
5. Bcrypt
6. Datetime
7. Uuid

## Getting Started
1. Install Python 3.11.1
2. Clone the project using https or ssh.
3. Once cloned, open the project in your code editor (PyCharm).
4. Inside the editor, open the terminal.
5. Check the python version. (Install Pyenv)
    ```
    python --version
    ```
6. Change the version of python.
    ```
    pyenv shell 3.11.1
    ```
7. Create a virtual environment.
    ```
    python -m venv .venv
    ```
8. Enter the virtual environment.
    ```
    source .venv/bin/activate
    ```
9. Change the python interpreter to .venv 3.11.1
10. Update PIP
    ```
    pip install --upgrade pip
    ```
11. Install the requirements.
    ```
    pip install -r requirements.txt
    ```
12. Verify that it is installed.
    ```
    pip freeze
    ```
13. Before running the project you must install PostgreSQL 
and create your database and its user with password. 
In the [documentation](https://docs.google.com/document/d/10AUeQ7tSZ2LV0SrCbiuQ6fT6TCXP_sGxoHqRno5LV70/edit?usp=sharing) 
are the steps to replace that 
data within the project
14. To run the project uses the following command.
    ```
     flask --app main run --debug 
    ```

## Documentation 
Click on the following link to view the documentation.
[Proyect documentation](https://docs.google.com/document/d/10AUeQ7tSZ2LV0SrCbiuQ6fT6TCXP_sGxoHqRno5LV70/edit?usp=sharing)