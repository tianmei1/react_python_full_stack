from app import db

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    text = db.Column(db.String(1000))
    image = db.Column(db.String(200))
    table = db.Column(db.String(1000))
    graph_data = db.Column(db.String(1000))
