#coding: utf-8

from flask import Blueprint, render_template, request

bp_home = Blueprint('home', __name__, url_prefix='/home', template_folder='templates')

@bp_home.route("/", methods=['POST'])
def home():
    return render_template("home.html")


