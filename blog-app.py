import os
from app import create_app, db
from models import User,Role
from flask_migrate import Migrate


app  = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)



@app.shell_context_processor
def make_shell_ontext:
    return dict(db=db,User=User,Role=Role)