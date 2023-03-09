from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/')
def landing_page():
    return render_template("landing_page.html")

@views.route('/home')
def home():

    return render_template("index.html")


