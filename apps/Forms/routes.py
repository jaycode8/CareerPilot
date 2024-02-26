from flask import Blueprint
from flask import render_template

forms_bp = Blueprint("forms", __name__, template_folder="templates")

@forms_bp.route("/")
def index():
    return render_template("sign-in.html")

@forms_bp.route("/resetpassword")
def passwordrecovery():
    return render_template("reset-password.html")

@forms_bp.route("/signup-user")
def jobseeker():
    return render_template("sign-up-user.html")

@forms_bp.route("/signup-employer")
def employer():
    return "employer"
    # return render_template("login.html")
