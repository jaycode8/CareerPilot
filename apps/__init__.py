from flask import Flask
from .jaymoh import routes as rt
from .about import routes as about_routes
from .Companies import routes as employer_routes
from .Jobs import routes as jobs_routes
from .contacts import routes as contact_routes
from .Forms import routes as forms_routes
from .Profile import routes as profile_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(rt.main_bp, url_prefix="/home")
    app.register_blueprint(about_routes.about_bp, url_prefix="/aboutus")
    app.register_blueprint(employer_routes.employers_bp, url_prefix="/companies")
    app.register_blueprint(jobs_routes.jobs_bp, url_prefix="/jobs")
    app.register_blueprint(contact_routes.contact_bp, url_prefix="/contacts")
    app.register_blueprint(forms_routes.forms_bp, url_prefix="/forms")
    app.register_blueprint(profile_routes.profile_bp, url_prefix="/profile")
    return app
