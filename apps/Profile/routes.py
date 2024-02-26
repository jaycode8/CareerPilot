from flask import Blueprint, render_template

profile_bp = Blueprint("profile", __name__, template_folder="templates")

@profile_bp.route("/")
def index():
    return render_template("profile.html")

