from flask import Blueprint
from flask import render_template

main_bp = Blueprint("main", __name__, template_folder="templates", static_folder="static")

@main_bp.route("/")
def index():
    categories = [1,2,3,4,5,6,7,8]
    return render_template("index.html", categories=categories)
