class Role(db.Model):
    __table_name  = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),unique=True)

    def __repr__(self):
        return <'Role %r', % self.name>


class User(db.Model):
    __table_name  = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64),unique=True, index=True)


    def __repr__(self):
        return <'Role %r', % self.name>



