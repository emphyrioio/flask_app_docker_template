from app.extensions import db_bp1


class Person(db_bp1.Model):
    __bind_key__ = "blueprint1"
    __tablename__ = "people"
    id = db_bp1.Column(db_bp1.Integer, primary_key=True)
