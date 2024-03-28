from flask import Blueprint, request
from flask import render_template
from apps.Forms.models import Jobs, Utils
from datetime import datetime

jobs_bp = Blueprint("jobs", __name__, template_folder="templates")

def time_conversions(date_time):
    date_string = datetime.strptime(str(date_time),'%Y-%m-%d %H:%M:%S.%f')
    secs = (datetime.now() -date_string).total_seconds()
    days_difference = int(secs//(24*3600))
    if days_difference == 0:
        dt = "Today"
    elif days_difference == 1:
        dt = "1 day ago"
    elif days_difference < 7:
        dt = f"{days_difference} days ago"
    elif days_difference < 30:
        dt = f"{days_difference//7} weeks ago"
    else:
        dt = f"{days_difference//30} months ago"
    return dt

@jobs_bp.route("/")
def index():
    jobs = Jobs.objects.all()
    categories = Utils.job_categories()
    job_types = Utils.job_type()
    for job in jobs:
        job.created_at = time_conversions(job.created_at)
    return render_template("jobs.html", jobs=jobs, categories=categories, job_types=job_types)

@jobs_bp.route("/<id>")
def job(id):
    job = Jobs.objects.get(id=id)
    jobs = Jobs.objects.all()
    job.created_at = time_conversions(job.created_at)
    return render_template("specificjob.html", relatedjobs=jobs, job=job)

@jobs_bp.route("/category/<category>")
def categories(category):
    jobs = Jobs.objects(category = category)
    categories = Utils.job_categories()
    job_types = Utils.job_type()
    for job in jobs:
        job.created_at = time_conversions(job.created_at)
    return render_template("jobs.html", jobs=jobs, category=category, categories=categories, job_types=job_types)

@jobs_bp.route("/companies/<id>")
def CompanyJobs(id):
    jobs = Jobs.objects(company = id)
    categories = Utils.job_categories()
    job_types = Utils.job_type()
    for job in jobs:
        job.created_at = time_conversions(job.created_at)
    return render_template("jobs.html", jobs=jobs, category=jobs[0].company.name,categories=categories, job_types=job_types)
