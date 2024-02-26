from flask import Blueprint
from flask import render_template

contact_bp = Blueprint("contact", __name__, template_folder="templates")

@contact_bp.route("/")
def index():
    contact = [1,2,3]
    return render_template("contacts.html", contacts=contact)
