import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
from utils import User

load_dotenv()
app = Flask(__name__)

user = User()

URL = "http://127.0.0.1:5000"
PAGES = [
    {"name": "Education", "href": URL + "/" + "education"},
    {"name": "Work Experience", "href": URL + "/" + "work"},
    {"name": "About Me", "href": URL + "/" + "about_me"},
    {"name": "Hobbies", "href": URL + "/" + "hobbies"},
    ]
    
@app.route('/', endpoint='index')
def index():
    return render_template('index.html',
                           education=user.education,
                           work_experience=user.work_experience,
                           hobbies=user.hobbies,
                           title="MLH Fellow",
                           url=os.getenv("URL"))

@app.route('/projects')
def projects():
    return render_template('projects.html',
                           projects=user.projects)

@app.route('/work_experience')
def work_experience():
    return render_template('work_exp.html',
                           work_experience=user.work_experience,)

@app.route('/hobbies', endpoint='hobbies')
def hobbies():
    return render_template('hobbies.html',
                           hobbies=user.hobbies,
                           url=os.getenv("URL"))
