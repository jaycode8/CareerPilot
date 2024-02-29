
from flask_mongoengine import MongoEngine

def mongo(app):
    app.config["MONGODB_SETTINGS"] = {"host":"mongodb://localhost:27017/careerpilot"}
    db.MongoEngine(app)
