from flask import Blueprint
from flask import render_template

jobs_bp = Blueprint("jobs", __name__, template_folder="templates")

@jobs_bp.route("/")
def index():
    data = [1,2,3,4,5,6,7,8,9]
    return render_template("jobs.html", jobs=data)

@jobs_bp.route("/<name>")
def job(name):
    rel = [1,2]
    return render_template("specificjob.html", relatedjobs=rel)
