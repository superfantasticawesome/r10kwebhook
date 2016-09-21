#!/usr/bin/env python

import os
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'r10k deployment'
@app.route('/deploy', methods=['GET', 'POST'])
def deploy():
    if request.method == 'GET':
        return 'OK'
    elif request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))
        r10kcmd = '/opt/puppetlabs/puppet/bin/r10k'
        print ('Deploying ' + data['environment'] + ' with R10k')
        os.system(r10kcmd + ' deploy environment ' + data['environment'] + ' -p ' )
        return json.dumps({'msg': 'Hi!'})


if __name__ == "__main__":
    app.run()
