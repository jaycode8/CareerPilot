from flask import Blueprint
from flask import render_template
from apps.Forms.models import Company

employers_bp = Blueprint("employers", __name__, template_folder="templates")

@employers_bp.route("/")
def index():
    companies = Company.objects.all()
    return render_template("companies.html", companies=companies)

@employers_bp.route("/<name>")
def employer(name):
    company_data = Company.objects.get(id=name)
    return render_template("company.html", data=company_data)
