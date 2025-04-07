import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure_app(app):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(base_dir, "database.db")}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = os.path.join(base_dir, "uploads")
    app.config['COMPRAS_FOLDER'] = os.path.join(base_dir, "imgs_compras")
