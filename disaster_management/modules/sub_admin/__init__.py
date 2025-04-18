from flask import Blueprint, render_template,request,redirect, url_for,flash, jsonify, session
from disaster_management.models import create_mongo_client, init_database, init_collection
from bson import ObjectId 
from pprint import pprint 

req_coll = ["sub_admin", "Volunteers"]
dbs = {name: init_collection(init_database(create_mongo_client(), "Disaster-ManagementDB"), name) for name in req_coll}
collection = dbs["Volunteers"]
sub_admin = Blueprint('sub_admin', __name__)

@sub_admin.route('/sub-admin-login', methods=["GET", "POST"])
def sub_admin_login():
    if request.method != "POST":
        return render_template('sub_admin/login.html')
    email = request.form.get("email")
    password = request.form.get("password")

    if sub_admin_login_data := dbs["sub_admin"].find_one({"email": email}):
        if sub_admin_login_data.get("password") == password:
            session['sub_admin_email'] = email
            flash("Login successful", category='success')
            return redirect(url_for("sub_admin.sub_admin_dash"))
        else:
            flash("Invalid password. Please try again.", category='error')
            return redirect(url_for("sub_admin.sub_admin_login"))
    else:
        flash("UserName Not Found. Please try again.", category='error')
        return redirect(url_for("sub_admin.sub_admin_login"))

@sub_admin.route('/sub-admin-logout')
def sub_admin_logout():
    session.pop('sub_admin_email', None)
    flash("You have been logged out", category='success')
    return redirect(url_for('sub_admin.sub_admin_login'))

@sub_admin.route("/sub-admin-dash")
def sub_admin_dash():
    if 'sub_admin_email' in session:
        data = list(collection.find({"sub_admin_email": session["sub_admin_email"]},{"name": 1, "age": 1, "gender": 1, "_id": 0 }))
        return render_template("sub_admin/adminDash.html", data=data)
    flash("You need to login first", category='error')
    return redirect(url_for("sub_admin.sub_admin_login"))    

@sub_admin.route("/sub-admin-add-vol", methods=['GET', 'POST'])
def sub_admin_add_vol():
    if 'sub_admin_email' not in session:
        flash("You need to login first", category='error')
        return redirect(url_for("sub_admin.sub_admin_login"))
    if request.method != "POST":
        return render_template("sub_admin/addVol.html")
    name = request.form.get("name")
    age = request.form.get("age")
    email = request.form.get("email")
    phone_no = request.form.get("phno")
    area = request.form.get('area')
    skills = request.form.get("role")
    gender = request.form.get("gender")
    pincode = request.form.get("pincode")
    password = request.form.get("password")

    if collection.find_one({'email': email}):
        flash('Email already exists. Please use a different email.', 'error')
        return redirect(url_for('sub_admin.sub_admin_add_vol'))

    volunteer_data = {
        'name': name,
        'age': age,
        'phone_no': phone_no,
        'email': email,
        'area': area,
        "skills": skills,
        "gender": gender ,
        "pincode": pincode,
        'password': password,
        "sub_admin_email":  session['sub_admin_email']
    }
    collection.insert_one(volunteer_data)
    flash('Registration successful!', 'success')
    return redirect(url_for('sub_admin.sub_admin_add_vol'))

