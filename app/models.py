from app import db

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(64), index=True, nullable=False)
    model = db.Column(db.String(120), index=True, nullable=False)
    extcolor = db.Column(db.String(120), index=True, nullable=False)
    intcolor = db.Column(db.String(120), index=True, nullable=False)
    transmission = db.Column(db.String(120), index=True, nullable=False)
    price = db.Column(db.String(120), index=True, nullable=False)
    contact = db.Column(db.String(120), index=True, nullable=False)