from flask import Blueprint
from flask import render_template

about_bp = Blueprint("about", __name__, template_folder="templates")

@about_bp.route("/")
def index():
    return render_template("about.html")
