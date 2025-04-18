from flask import Blueprint, render_template,request,redirect, url_for,flash, jsonify, session
from disaster_management.models import create_mongo_client, init_database, init_collection
from bson import ObjectId 
from datetime import datetime
from pprint import pprint

req_coll = ["Volunteers", "funds"]
dbs = {name: init_collection(init_database(create_mongo_client(), "Disaster-ManagementDB"), name) for name in req_coll}
collection = dbs['Volunteers'] 
vol = Blueprint('vol', __name__)



@vol.route('/vol-login', methods=["GET", "POST"])
def vol_login():
    if request.method != "POST":
        return render_template('vol/vol_login.html')
    email = request.form.get("email")
    password = request.form.get("password")
    print(email, password)

    if vol_login_data := collection.find_one({"email": email}):
        if vol_login_data.get("password") == password:
            session['vol_email'] = email
            flash("Login successful", category='success')
            return redirect(url_for("vol.vol_dash_2"))
        else:
            flash("Invalid password. Please try again.", category='error')
            return redirect(url_for("vol.vol_login"))
    else:
        flash("Email Not Found. Please register and try again.", category='error')
        return redirect(url_for("vol.vol_reg"))


@vol.route("/vol-reg", methods=['GET', 'POST'])
def vol_reg():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        phone_no = request.form.get("phno")
        area = request.form.get('area')
        skills = request.form.get("role")
        pincode = request.form.get("pincode")
        password = request.form.get("password")
        email = request.form.get("email")
        if collection.find_one({'email': email}):
            flash('Email already exists. Please use a different email.', 'error')
            return redirect(url_for('vol.vol_reg'))
        vol_data = {
            'name': name,
            'age': age,
            'phone_no': phone_no,
            'email': email,
            'area': area,
            "skills": skills,
            "pincode": pincode,
            'password': password
        }
        collection.insert_one(vol_data)
        flash('Registration successful!', category='success')
        return redirect(url_for('vol.vol_login')) 
    else:
        return render_template("vol/vol_reg.html")
    
@vol.route("/vol-dash", methods=['GET', 'POST'])
def vol_dash():
    if 'vol_email' in session:
        flash("You already logged in", category='error')
        return redirect(url_for("vol.vol_dash_2"))
    return render_template("vol/vol_dash.html")


@vol.route("/vol-dash-2", methods=['GET', 'POST'])
def vol_dash_2():
    if 'vol_email' not in session:
        flash("You need to login first", category='error')
        return redirect(url_for("vol.vol_login"))
    return render_template("vol/vol_dash_2.html")

    
@vol.route("/vol-pay", methods=['POST','GET'])
def vol_pay():
    if 'vol_email' not in session:
        flash("You need to login first", category='error')
        return redirect(url_for("vol.vol_login"))
    if request.method == "POST":
        amt = request.form.get("amt")
        accno = request.form.get("accno")
        email = session['vol_email']
        name = collection.find_one({"email":email}).get('name')
        data = {
            "name": name,
            "accno": accno,
            "email": email,
            "amt": amt,
            "pay_from": "vol",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        dbs['funds'].insert_one(data)
        return redirect(url_for('vol.vol_dash_2'))
    return redirect(url_for('vol.vol_dash_2'))

@vol.route('/vol-logout')
def vol_logout():
    session.pop('vol_email', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('vol.vol_dash'))


@vol.route("/map", methods=['GET', 'POST'])
def map():
    return render_template("vol/map.html")


@vol.route("/vol_start", methods=['GET', 'POST'])
def vol_start():
    return "start volunteering"
