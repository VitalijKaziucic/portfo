from cgitb import html
from crypt import methods
from html.entities import html5
import imp
from flask import Flask, render_template, request, redirect
from save_data import write_data


app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


# @app.route("/login", methods=["POST", "GET"])
# def login():
#     if request.method == "POST":
#         data = request.form.to_dict()
#         if data["username"] == "Vitalij":
#             return render_template("index.html")
#         else:
#             return data


@app.route("/<string:page_name>")
def open_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    print(request.method)
    if request.method == "POST":
        data = request.form.to_dict()
        write_data("./database.txt", data.values())
        return redirect("/thank_you.html")


@app.route('/template', methods=['GET', 'POST'])
def template():
    if request.method == 'POST':
        return "Hello"
    # return render_template('index.html')
