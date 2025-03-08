import os
import git 
from datetime import datetime, timedelta
from flask import Flask, render_template

app = Flask(__name__)

repo_path = "https://github.com/HyunwooKim04/BAEKJOON" #본인의 Github 경로로 바꾸기

one_month_ago = datetime.now() - timedelta(days=30)

def get_old_files():
    repo = git.Repo(repo_path)
    commits = list(repo.iter_commits('master'))
    changed_files = set()

    for commit in commits:
        commit_date = datetime.fromtimestamp(commit.committed_date)

        if commit_date < one_month_ago:
            for diff in commit.diff(commit.parents or None):
                chaged_files.add(diff.a_path)

    return list(changed_files)

def index():
    old_files = get_old_files()
    return render_template('index.html', files=old_files)

if __name__ == '__main__':
    app.run(debug=True)
