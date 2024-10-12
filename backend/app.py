from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable cross-origin resource sharing
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reports.db'
db = SQLAlchemy(app)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    text = db.Column(db.String(1000))
    image = db.Column(db.String(200))
    table = db.Column(db.String(1000))
    graph_data = db.Column(db.String(1000))

@app.route('/api/reports', methods=['POST'])
def save_report():
    data = request.json
    report = Report(
        title=data['title'],
        text=data['text'],
        image=data['image'],
        table=str(data['table']),
        graph_data=str(data['graphData'])
    )
    db.session.add(report)
    db.session.commit()
    return jsonify({'message': 'Report saved'}), 201

@app.route('/api/reports/random', methods=['GET'])
def get_random_report():
    sample_data = {
        "title": "Sample Report",
        "text": "This is a randomly generated report.",
        "image": "https://via.placeholder.com/150",
        "table": [["Item 1", "Item 2"], ["Data 1", "Data 2"]],
        "graphData": [10, 20, 30, 40]
    }
    return jsonify(sample_data)

if __name__ == '__main__':
    db.create_all()  # Initialize the SQLite database
    app.run(debug=True)
