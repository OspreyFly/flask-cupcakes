from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

"""Models for Cupcake app."""
class Cupcake(db.Model):
    __tablename__ = "cupcakes"
    id  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.String(60), nullable=False)
    size = db.Column(db.String(60), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(200), nullable=False, default="https://tinyurl.com/demo-cupcake")

    def serialize(self):
        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image,
        }