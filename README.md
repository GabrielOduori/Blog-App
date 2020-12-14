# Blog-app
Blog application with Python,Flask and PostgreSQL



## Set-up Requirements

### Prerequisites
* python3.8
* Flask 1.1
* Virtualenv


### Technologies

-Bootstrap4
-CSS3

### Cloning
* In your terminal:
        
        $ git clone https://github.com/GabrielOduori/Blog-App
        $ cd Blog-App

## Running the Application
* Creating the virtual environment

        $ python3 -m pip install --user virtualenv ( on a Mac)
        $ python3 -m virtualenv env
        $ source env/bin/activate
        $(For other operating systems, see https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
        
* Installing Flask and other Modules
- While in the virtal environment install all the requirements by running 

        $ pip install -r requirements.txt


* Database

        $ flask db init
        $ flask db migrate -m"Add migration Message"
        $ flask db upgrade
        
* Running the app

        $ export FLASK_APP=blog-app.py(set FLASK_APP=blog-app.py)
        $ export FLASK_DEBUG=1 (set FLASK_DEBUG=1)
        $ flask run
