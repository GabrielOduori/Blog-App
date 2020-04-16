# Blog-app
Blog application with Python,Flask and PostreSQL



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
        
        $ git clone https://github.com/GabrielOduori/Blog-Post
        $ cd Blog-Post

## Running the Application
* Creating the virtual environment

        $ python3 -m pip install --user virtualenv ( on a Mac)
        $ python3 -m virtualenv env
        $ source env/bin/activate
        $(For other operating systems, see https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
        
* Installing Flask and other Modules
- While in the virtalenvironment install all the requirements by running 
$ pip install -r requirements.txt

* Database
        $ flask db init
        $ flask db migrate -m"Message"
        $ flask db upgrade 

* Running the app
        $ set FLASK_APP=blog-app.py (export FLASK_APP=blog-app.py )
        $ set FLASK_DEBUG=1 (export FLASK_DEBUG=1 )
        $ flask run