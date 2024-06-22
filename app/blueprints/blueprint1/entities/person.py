from app.extensions import db


class PersonBp1(db.Model):
    __tablename__ = "people"
    id = db.Column(db.Integer, primary_key=True)
    first_names = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    birth_city = db.Column(db.String(100), nullable=False)
    birth_postal_code = db.Column(db.Integer, nullable=False)
    birth_country = db.Column(db.String(100), nullable=False)
    death_date = db.Column(db.Date, nullable=True)
    death_city = db.Column(db.String(100), nullable=True)
    death_postal_code = db.Column(db.Integer, nullable=True)
    death_country = db.Column(db.String(100), nullable=True)
    unique_hash = db.Column(db.String(250), unique=True, nullable=False, index=True)
