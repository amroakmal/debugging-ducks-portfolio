import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
from utils import User

load_dotenv()
app = Flask(__name__)

user = User()

hobbies_arr = ["Football", "Video Games", "Watching Aurora"]
work_experience = ["SWE @ Incorta     2021-2024", "SWE Intern @ M3ntorship      01/2021-04/2021"]
education = ["M.Sc. @ TTU     2024-2026", "B.Sc. @ Alexandria University    2026-2021"]
URL = "http://127.0.0.1:5000"
pages = [
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
