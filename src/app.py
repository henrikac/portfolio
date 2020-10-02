from datetime import datetime

from github import Github
from flask import Flask, render_template

from settings import ACCESS_TOKEN


app = Flask(__name__)


gh = Github(ACCESS_TOKEN)


@app.route('/')
def index():
    now = datetime.utcnow()
    interests = [
            'Software development',
            'Machine learning',
            'Artificial intelligence',
            'Outer space']
    repos = gh.get_user().get_repos()

    return render_template('index.html', now=now, repos=repos, interests=interests)

