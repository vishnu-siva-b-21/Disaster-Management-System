from flask import Blueprint, render_template,request,redirect, url_for,flash, jsonify

main = Blueprint('main', __name__)

@main.route("/")
def home():
        return render_template("main/home.html")
