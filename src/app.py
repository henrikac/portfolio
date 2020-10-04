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
    ]
    repo_names = [
            'npy',
            'SocialBots',
            'MoodleScheduleScraper',
            'JokeScraper',
            'P2Bot',
            'ThePeriodicTable',
    ]
    repos = [repo for repo in gh.get_user().get_repos() if repo.name in repo_names]

    return render_template('index.html', now=now, repos=repos, interests=interests)

