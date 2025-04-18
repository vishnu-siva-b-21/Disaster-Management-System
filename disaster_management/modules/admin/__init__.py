from flask import Blueprint, render_template,request,redirect, url_for,flash, jsonify
from disaster_management.models import create_mongo_client, init_database, init_collection
from bson import ObjectId
from pprint import pprint 

req_coll = ["Volunteers", "sub_admin"]
dbs = {name: init_collection(init_database(create_mongo_client(), "Disaster-ManagementDB"), name) for name in req_coll}

admin = Blueprint('admin', __name__)

@admin.route("/vol-details")
def vol_details():
		vol_details = list(dbs["Volunteers"].find({},{"name":1, "age":1, "gender":1, "phone_no":1, "area":1, "pincode":1, "skills":1, "email":1, "sub_admin_email":1, "_id":0}))
		return render_template("admin/vol_details.html",vol_details=vol_details)

@admin.route("/sub-admin-details")
def sub_admin_details():
		sub_admin_details = list(dbs["sub_admin"].find({},{"name":1, "age":1, "gender":1, "phone_no":1, "area":1, "pincode":1, "skills":1, "email":1, "sub_admin_email":1, "_id":0}))
		return render_template("admin/sub_admin_details.html",sub_admin_details=sub_admin_details)


@admin.route("/add-sub-admin", methods=['GET', 'POST'])
def add_sub_admin():
	if request.method != "POST":
		return render_template("admin/add_sub_admin.html")
	name = request.form.get("name")
	age = request.form.get("age")
	email = request.form.get("email")
	phone_no = request.form.get("phno")
	area = request.form.get('area')
	gender = request.form.get("gender")
	pincode = request.form.get("pincode")
	password = request.form.get("password")

	if dbs["sub_admin"].find_one({'email': email}):
		flash('Email already exists. Please use a different email.', 'error')
		return redirect(url_for('admin.add_sub_admin'))

	sub_admin_data = {
		'name': name,
		'age': age,
		'phone_no': phone_no,
		'email': email,
		'area': area,
		"gender": gender ,
		"pincode": pincode,
		'password': password,
	}
	
	dbs["sub_admin"].insert_one(sub_admin_data)
	flash('Registration successful!', 'success')
	return redirect(url_for('admin.add_sub_admin'))

@admin.route("/affected-people")
def affected_people():
		return render_template("admin/affected_people.html")

@admin.route("/funds-collected")
def funds_collected():
		return render_template("admin/funds_collected.html")

@admin.route("/funds-given")
def funds_given():
		return render_template("admin/funds_given.html")


@admin.route("/send_loc")
def send_loc():
	data = dbs["end_user"]
	results = list(data.find({}, {'_id': 0, "Pincode":1}))
	
	# Assuming you have a condition to determine danger status
	for result in results:
		result["danger"] = True 

	return jsonify(results), 200

@admin.route("/map")
def map():
		return render_template("admin/map.html")