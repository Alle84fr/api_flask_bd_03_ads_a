from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="user", lazy=True)

    def __repr__(self):
        return f"<User {self.name}>"
