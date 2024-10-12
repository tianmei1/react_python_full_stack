from flask import Flask, request, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_reuploaded import UploadSet, configure_uploads, IMAGES



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reports.db'
app.config['UPLOADED_IMAGES_DEST'] = 'uploads/images'  # Folder to save uploaded images
db = SQLAlchemy(app)

# Set up file upload for images
images = UploadSet('images', IMAGES)
configure_uploads(app, images)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    text = db.Column(db.String(1000))
    image = db.Column(db.String(200))  # Image URL or filename
    table = db.Column(db.String(1000))
    graph_image = db.Column(db.String(200))  # Stores image URL for graphs

@app.route('/api/upload_image', methods=['POST'])
def upload_image():
    if 'image' in request.files:
        filename = images.save(request.files['image'])
        image_url = url_for('static', filename=f'uploads/images/{filename}', _external=True)
        return jsonify({'image_url': image_url})
    return jsonify({'error': 'No image uploaded'}), 400

@app.route('/api/reports', methods=['POST'])
def save_report():
    data = request.json
    report = Report(
        title=data['title'],
        text=data['text'],
        image=data['image'],
        graph_image=data['graphImage']
    )
    db.session.add(report)
    db.session.commit()
    return jsonify({'message': 'Report saved'}), 201
