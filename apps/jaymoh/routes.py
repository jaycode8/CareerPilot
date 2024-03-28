from flask import Blueprint, request, render_template
from apps.Forms.models import Utils

main_bp = Blueprint("main", __name__, template_folder="templates", static_folder="static")

@main_bp.route("/")
def index():
    categories = Utils.job_categories()
    return render_template("index.html", categories=categories)
