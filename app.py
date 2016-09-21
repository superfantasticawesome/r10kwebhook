#!/usr/bin/env python

import os
from flask import Flask, request
from  flask.ext.runner import Runner
import json

app = Flask(__name__)
app.config.from_pyfile('config.py')
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
        os.system(
                app.config['R10K'] + 
                ' deploy environment ' + 
                data['environment'] + 
                ' -p -vv -c ' + 
                app.config['R10K_CONF'] )
        return json.dumps({'msg': 'Hi!'})


if __name__ == "__main__":
    runner.run()
