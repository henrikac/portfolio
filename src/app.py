from github import Github
from flask import Flask, render_template

from settings import ACCESS_TOKEN


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

