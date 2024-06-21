import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
from utils import User

load_dotenv()
app = Flask(__name__)

user = User()

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
    return render_template('hobbies.html', hobbies=hobbies_arr, url=os.getenv("URL"))
