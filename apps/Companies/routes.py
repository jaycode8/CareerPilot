from flask import Blueprint
from flask import render_template

employers_bp = Blueprint("employers", __name__, template_folder="templates")

@employers_bp.route("/")
def index():
    data = [1,2,3,4,5,6,7,8]
    return render_template("companies.html", companies=data)

@employers_bp.route("/<name>")
def employer(name):
    return render_template("company.html")
