from flask import Blueprint, render_template, jsonify, session, request, flash, redirect, url_for
from disaster_management.models import create_mongo_client, init_database, init_collection
from bson import ObjectId 
from datetime import datetime
from pprint import pprint


req_coll = ["Organizations", 'funds']
dbs = {name: init_collection(init_database(create_mongo_client(), "Disaster-ManagementDB"), name) for name in req_coll}
collection = dbs['Organizations'] 
org = Blueprint('org', __name__)


@org.route('/org-login', methods=["GET", "POST"])
def org_login():
    if request.method != "POST":
        return render_template('org/org_login.html')
    email = request.form.get("email")
    password = request.form.get("password")
    print(email, password)

    if org_login_data := collection.find_one({"email": email}):
        if org_login_data.get("password") == password:
            session['org_email'] = email
            flash("Login successful", category='success')
            return redirect(url_for("org.org_dash_2"))
        else:
            flash("Invalid password. Please try again.", category='error')
            return redirect(url_for("org.org_login"))
    else:
        flash("Email Not Found. Please register and try again.", category='error')
        return redirect(url_for("org.org_reg"))

@org.route("/org_reg", methods=["POST", "GET"])
def org_reg():
    if request.method != "POST":
        return render_template("org/org_reg.html")
    organization_name = request.form["Organization Name"]
    in_charge_name = request.form["In-Charge name"]
    phone_no = request.form["Phone Number"]
    email = request.form['Email_ID']
    password = request.form["Password"]

    if collection.find_one({'email': email}):
        flash('Email already exists. Please use a different email.', 'error')
        return redirect(url_for('org.org_reg'))

    user_data = {
        'org_name': organization_name,
        'in_charge_name': in_charge_name,
        'phone_no': phone_no,
        'email': email,
        'password': password
    }

    collection.insert_one(user_data)
    flash('Registration successful!', 'success')
    return redirect(url_for('org.org_dash'))

@org.route("/org-dash", methods=['GET', 'POST'])
def org_dash():
    if 'org_email' in session:
        flash("You already logged in", category='error')
        return redirect(url_for("org.org_dash_2"))
    orgs = list(collection.find({},{"org_name":1, "_id":0}))
    return render_template("org/org_dash.html", orgs=orgs)


@org.route("/org-dash-2", methods=['GET', 'POST'])
def org_dash_2():
    if 'org_email' not in session:
        flash("You need to login first", category='error')
        return redirect(url_for("org.org_login"))
    return render_template("org/org_dash_2.html")


@org.route('/org-logout')
def org_logout():
    session.pop('org_email', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('org.org_dash'))


@org.route("/org-pay", methods=["GET", "POST"])
def org_pay():
    if 'org_email' not in session:
        flash("You need to login first", category='error')
        return redirect(url_for("org.org_login"))
    if request.method == "POST":
        amt = request.form.get("amt")
        accno = request.form.get("accno")
        email = session['org_email']
        name = collection.find_one({"email":email}).get('org_name')
        data = {
            "name": name,
            "accno": accno,
            "email": email,
            "amt": amt,
            "pay_from": "org",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        dbs['funds'].insert_one(data)
        return redirect(url_for('org.org_dash_2'))
    return render_template("org/org_pay.html")


