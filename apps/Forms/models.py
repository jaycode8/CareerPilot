
from apps import db
import datetime

class Education(db.EmbeddedDocument):
    program = db.StringField(default="")
    school = db.StringField(default="")
    duration = db.StringField(default="")
    about = db.StringField(default="")

class Experience(db.EmbeddedDocument):
    title = db.StringField(default="")
    institution = db.StringField(default="")
    duration = db.StringField(default="")
    about = db.StringField(default="")

class Users(db.Document):
    username = db.StringField(required=True, unique=True)
    fullnames = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
    about = db.StringField(default="")
    education = db.ListField(db.EmbeddedDocumentField(Education))
    experience = db.ListField(db.EmbeddedDocumentField(Experience))
    skills = db.ListField(db.StringField(default=""))
    languages = db.ListField(db.StringField(default=""))
    profile_pic = db.StringField(default="")
    phone_number = db.StringField(default="")
    current_location = db.StringField(default="")
    social_media = db.DictField()
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)

class Company(db.Document):
    name = db.StringField(required=True, unique=True)
    ceoname = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
    description = db.StringField(default="", required=True)
    avatar = db.StringField(default="")
    coverImg = db.StringField(default="")
    website = db.StringField(default="")
    location = db.StringField(default="", required=True)
    dateFounded = db.DateTimeField(required=True)
    phone = db.StringField(required=True)
    social_media = db.DictField()
    jobs = db.ListField(db.ReferenceField('Jobs'))
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)

class Jobs(db.Document):
    title = db.StringField(required=True)
    job_type = db.StringField(required=True)
    category = db.StringField(required=True)
    position = db.StringField(required=True)
    salary = db.FloatField(required=True)
    experience = db.StringField(required=True)
    description = db.StringField(required=True)
    skills = db.ListField(db.StringField(default=""))
    responsibilities = db.StringField(default="")
    qualifications = db.StringField(default="")
    avatar = db.StringField(default="")
    cover = db.StringField(default="")
    company = db.ReferenceField(Company)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)

class Utils:
    def job_categories():
        return ["Information Technology", "Healthcare","Education","Finance","Marketting","Engineering","Human Resource","Hospitality","Construction","Manufacturing"]

    def job_type():
        return ["Full Time","Part Time", "Contract"]