from flask import Blueprint, render_template, request, redirect, url_for
from apps.Forms.models import Company, Users, Jobs

profile_bp = Blueprint("profile", __name__, template_folder="templates", static_folder="static")

@profile_bp.route("/")
def index():
    if request.cookies.get("user"):
        user_data = Users.objects.get(id = request.cookies.get("user"))
        return render_template("profile.html", user=user_data)
    else:
        return redirect(url_for('index'))


@profile_bp.route("/company")
def company():
    if request.cookies.get("user"):
        company = Company.objects.get(id = request.cookies.get("user"))
        return render_template("companyProfile.html", company=company, user="")
    else:
        return redirect(url_for('index'))
