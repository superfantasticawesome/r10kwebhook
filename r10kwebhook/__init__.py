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
        print("Deploying " + data['environment'])
        appdir = os.path.dirname(os.path.realpath(__file__))
        deploydir = (os.path.abspath(os.path.join(appdir, os.pardir)))
        deployscript = os.path.join(deploydir, 'deploy')
        subprocess.call(
                [
                    deployscript,
                    data['environment'],
                    app.config['R10K'],
                    app.config['R10K_CONF']
                    ]
                )
        return json.dumps(
                {
                    'r10k command': app.config['R10K'],
                    'environment': data['environment'],
                    'r10k config': app.config['R10K_CONF'] ,
                    }
                )


if __name__ == "__main__":
    runner.run()
