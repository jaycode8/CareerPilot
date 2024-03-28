from flask import Flask, request
from flask_mongoengine import MongoEngine
from config import Config

db = MongoEngine()
app = Flask(__name__)
app.config.from_object(Config)

@app.context_processor
def inject_user():
    from apps.Forms.models import Users, Company
    user_id = request.cookies.get("user")
    user_type = request.cookies.get("account_type")
    user = ""
    if user_id:
        if user_type == "jobseeker":
            user = Users.objects.get(id = user_id)
        elif user_type == "company":
            user = Company.objects.get(id = user_id)
            user.profile_pic = user.avatar
            user.username = user.name
        return {"current_user": user}
    return {"current_user": user}

def create_app():
    from .jaymoh import routes as rt
    from .about import routes as about_routes
    from .Companies import routes as employer_routes
    from .Jobs import routes as jobs_routes
    from .contacts import routes as contact_routes
    from .Forms import routes as forms_routes
    from .Profile import routes as profile_routes

    app.register_blueprint(rt.main_bp, url_prefix="/home")
    app.register_blueprint(about_routes.about_bp, url_prefix="/aboutus")
    app.register_blueprint(employer_routes.employers_bp, url_prefix="/companies")
    app.register_blueprint(jobs_routes.jobs_bp, url_prefix="/jobs")
    app.register_blueprint(contact_routes.contact_bp, url_prefix="/contacts")
    app.register_blueprint(forms_routes.forms_bp, url_prefix="/forms")
    app.register_blueprint(profile_routes.profile_bp, url_prefix="/profile")

    db.init_app(app)

    return app


