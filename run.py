#!/usr/bin/env python

import argparse

from r10kwebhook import app

parser = argparse.ArgumentParser()
parser.add_argument('--port', '-p', dest='port', default=8088)
parser.add_argument('--debug', '-d', dest='debug', default=True)
parser.add_argument('--host', dest='host', default='127.0.0.1')
args = parser.parse_args()


if __name__ == '__main__':
    app.run(debug=args.debug, port=int(args.port), host=args.host)
