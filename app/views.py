import requests
from flask import render_template, request
import clouds
from app import west

@west.route("/")
def show_home():
	"""Shows the daily top 10 of least cloud coverage."""
	return render_template("index.html")


@west.route("/clouds")
def show_clouds():
	"""Shows the daily top 10 of least cloud coverage."""
	return render_template("clouds.html", graph=clouds.get_graph())

@west.route("/map")
def show_map():
	"""Shows the map page."""
	return render_template("map.html")