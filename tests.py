#!/usr/bin/env python

import os
from r10kwebhook import app
import unittest
import tempfile
import json

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING']= True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index_(self):
        rv = self.app.get('/')
        assert rv.status_code == 200

    def test_index_content(self):
        rv = self.app.get('/')
        assert b'r10k deployment' in rv.data

    def test_deploy_get(self):
        rv = self.app.get('/deploy')
        assert rv.status_code == 200


if __name__ == '__main__':
    unittest.main()
