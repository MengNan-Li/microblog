#!/Users/lmn/anaconda2/envs/python36/bin/python
# -*- coding: utf-8 -*-
from app import app

app.run(debug = True)

'''
还有一种启动方式：
$ export FLASK_APP=__init__.py
$ export FLASK_DEBUG=1
$ flask run
'''