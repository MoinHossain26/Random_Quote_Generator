from flask import Blueprint, render_template
import requests
import random
import math

views = Blueprint("views", __name__)

# https://type.fit/api/quotes


@views.route("/", methods=["GET"])
def home():
    random_index = math.ceil(random.random() * 250)
    response = requests.get("https://type.fit/api/quotes")
    quote = response.json()
    return render_template("index.html", quote=quote[random_index])
