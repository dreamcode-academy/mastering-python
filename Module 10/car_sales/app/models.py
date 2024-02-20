from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Car(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    make = db.Column(db.String(100), nullable = False)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def _repr_(self):
        return f'<Car {self.make} {self.model} {self.year}>'