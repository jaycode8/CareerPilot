import os
from flask import Blueprint, jsonify, make_response, redirect, request_started, url_for, render_template
from werkzeug.utils import secure_filename
from apps import db
from .models import Company, Education, Experience, Jobs, Users, Utils
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
import cloudinary
from cloudinary.uploader import upload

forms_bp = Blueprint("forms", __name__, template_folder="templates")

@forms_bp.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        user = Users.objects(username=username).first()
        if user:
            passw = check_password_hash(user.password, password)
            if passw:
                res = make_response(redirect(url_for("index")))
                res.set_cookie("user", str(user.id))
                res.set_cookie("account_type", "jobseeker")
                return res
            error = "wrong password"
        else:
            error = "username does not exist"
        return render_template("sign-in.html", error=error)
    return render_template("sign-in.html")


@forms_bp.route("/resetpassword")
def passwordrecovery():
    return render_template("reset-password.html")


@forms_bp.route("/signup-user", methods=["GET", "POST"])
def jobseeker():
    error = None
    if request.method == "POST":
        username = request.form.get('username')
        fullnames = request.form.get("fullnames")
        password = request.form.get('password')
        email = request.form.get('email')
        educations = []
        experiences = []
        for i in range(3):
            edu_data = {
                "program":f"test program {i}",
                "school":f"test school {i}",
                "duration":f"test duration {i}",
                "about":f"test about school {i}"
            }
            educations.append(Education(**edu_data))
        for i in range(3):
            expe_data = {
                "title":f"title {i+1}",
                "institution":f"inst {i+1}",
                "duration":f"201{i+1}-201{i+2}",
                "about":f"test about experience {i+1}"
            }
            experiences.append(Experience(**expe_data))
        hashed_password = generate_password_hash(password)
        new_user = Users(username=username, fullnames=fullnames, password=hashed_password, email=email, education=educations, experience=experiences)
        try:
            new_user.save()
            return redirect(url_for("forms.index"))
        except:
            error = "user with above credetials exist"
        return render_template("sign-up-user.html", error=error)
    return render_template("sign-up-user.html")

@forms_bp.route("/update-user", methods=["GET", "POST"])
def updateUserProfile():
    if request.method == "POST":
        user_id = request.cookies.get("user")
        about = request.form.get("about")
        location = request.form.get("current_location")
        email = request.form.get("email")
        fullnames = request.form.get("fullname")
        languages = request.form.get("languages")
        phone = request.form.get("phone_number")
        skills = request.form.get("skills")
        username = request.form.get("username")
        profile = request.files['profile']

        fb = request.form.get("fb")
        xplatform = request.form.get("xplatform")
        linkedin = request.form.get("linkedin")
        whatsapp = request.form.get("whatsapp")

        lang_list = [language.strip() for language in languages.split((","))]
        skill_list = [skill.strip() for skill in skills.split((","))]
        user=Users.objects.get(id=user_id)
        if user:
            if profile:
                directory = "careerpilot/users"
                result = upload(profile, folder=directory)
                profile = result['url']
            else:
                profile = user.profile_pic
            user.update(about=about, current_location=location, email=email, fullnames=fullnames, phone_number=phone, username=username, languages=lang_list, skills=skill_list, profile_pic=profile)
            user.save()
            return redirect(url_for("profile.index"))
    return "get"

@forms_bp.route("/signincompany", methods=["GET", "POST"])
def signCompany():
    error = None
    if request.method == "POST":
        company = Company.objects(name=request.form.get("companyname")).first()
        if company:
            passw = check_password_hash(company.password, request.form.get("password"))
            if passw:
                res = make_response(redirect(url_for("index")))
                res.set_cookie("user", str(company.id))
                res.set_cookie("account_type", "company")
                return res
            error = "wrong password"
        else:
            error = "A company with that name not found"
        return render_template("signin-company.html", error=error)
    return render_template("signin-company.html")

@forms_bp.route("/signup-employer", methods=["GET", "POST"])
def employer():
    error = None
    if request.method == "POST":
        name = request.form.get("companyname")
        ceo = request.form.get("ceoname")
        email = request.form.get("email")
        password = request.form.get("password")
        desc = request.form.get("description")
        website = request.form.get("website")
        loc = request.form.get("location")
        ph = request.form.get("phone")
        dateFound = request.form.get("date")
        avatar = request.files["companyLogo"]
        hashed_password = generate_password_hash(password)
        if avatar:
            coverImg = request.files["companyCover"]
            directory = "careerpilot/companies"
            if coverImg:
                avatar_result = upload(avatar, folder=directory)
                avatar = avatar_result['url']
                cover_result = upload(coverImg, folder=directory)
                coverImg = cover_result['url']
                new_company = Company(name=name, ceoname=ceo,email=email,password=hashed_password, description=desc,website=website, location=loc, dateFounded = dateFound, avatar=avatar,coverImg=coverImg, phone=ph)
                try:
                    new_company.save()
                    return redirect(url_for("forms.signCompany"))
                except:
                    error ="Try again later"
            else:
                error =  "A company cover photo is required"
        else:
            error = "An avatar or company logo not provided"
        return render_template("signup-employer.html", error=error)
    return render_template("signup-employer.html")

@forms_bp.route("/jobs", methods=["GET","POST"])
def newJob():
    if request.method == "POST":
        title = request.form.get("title")
        jobtype = request.form.get("type")
        category = request.form.get("category")
        description = request.form.get("description")
        position = request.form.get("position")
        salary = request.form.get("salary")
        experience = request.form.get("experience")
        qualif = request.form.get("qualifications")
        respo = request.form.get("responsibilities")
        skills = request.form.get("skills")
        skill_list = [skill.strip() for skill in skills.split((","))]
        coverImg = request.files["jobcover"]
        if coverImg:
            directory = "careerpilot/jobs"
            result = upload(coverImg, folder=directory)
            coverImg = result['url']
            new_job = Jobs(title=title, job_type=jobtype, category=category, position=position, salary=salary, description=description, skills=skill_list, responsibilities=respo, experience=experience,qualifications=qualif, cover=coverImg, company=request.cookies.get("user"))
            try:
                new_job.save()
                Company.objects(id=request.cookies.get("user")).update_one(push__jobs=new_job.id)
                return redirect(url_for("profile.company"))
            except ValueError as e:
                error ="Try again later"
                print(e)
        else:
            error =  "A cover photo is required"
            print("err2")
        return request.form
    categories = Utils.job_categories()
    job_types = Utils.job_type()
    return render_template("addJob.html", jobtypes=job_types, categories=categories)

@forms_bp.route("/job/<id>")
def delJob(id):
    job = Jobs.objects.get(id=id)
    # TODO implement deletion of the image file later
    job.delete()
    return redirect(url_for("profile.company"))

@forms_bp.route("/logout")
def logOut():
    res = make_response(redirect(url_for("index")))
    res.delete_cookie("user")
    res.delete_cookie("account_type")
    return res


