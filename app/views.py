import requests
from flask import render_template, request
from app import west

@west.route("/")
def show_home():
	"""Shows the home page."""
	return render_template("index.html")