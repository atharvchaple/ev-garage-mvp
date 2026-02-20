from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200), nullable=False)


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, nullable=False)
    vehicle_type = db.Column(db.String(10), nullable=False)   # 2W / 3W
    model_name = db.Column(db.String(100), nullable=False)
    registration_number = db.Column(db.String(50), nullable=False)

class Battery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(20), nullable=False)


class ServiceRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(20), nullable=False)
    problem = db.Column(db.String(200), nullable=False)
    work = db.Column(db.String(200), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
