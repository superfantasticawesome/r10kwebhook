#!/usr/bin/env python

import os
from flask import Flask, request
from  flask.ext.runner import Runner
import json
import subprocess

app = Flask(__name__)
app.config.from_pyfile('../config.py')
runner = Runner(app)

@app.route('/')
def index():
    return 'r10k deployment'
@app.route('/deploy', methods=['GET', 'POST'])
def deploy():
    if request.method == 'GET':
        return 'OK'
    elif request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))
        if 'X-GitHub-Event' in request.headers or 'X-Gitlab-Event' in request.headers: # GitHub/GitLab
            environment = data['ref'].split('/')[-1]
        elif 'X-Event-Key' in request.headers: # Atlassian
            environment = 'push']['changes'][0]['new']['name']
        elif 'environment' in data: # Original behavior
            environment = data['environment']
        else: # Default to GitHub/GitLab
            environment = data['ref'].split('/')[-1]
        print("Deploying " + environment)
        appdir = os.path.dirname(os.path.realpath(__file__))
        deploydir = (os.path.abspath(os.path.join(appdir, os.pardir)))
        deployscript = os.path.join(deploydir, 'deploy')
        subprocess.call(
                [
                    deployscript,
                    environment,
                    app.config['R10K'],
                    app.config['R10K_CONF']
                    ]
                )
        return json.dumps(
                {
                    'r10k command': app.config['R10K'],
                    'environment': environment,
                    'r10k config': app.config['R10K_CONF'] ,
                    }
                )


if __name__ == "__main__":
    runner.run()
