import os
basedir = os.path.abspath(os.path.dirname(__file__))


def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'library.db')

CSRF_ENABLED = True
SECRET_KEY = '*\x8c3\xab\xacN:W\x88x\xc0}\xe4\xc5\xc2E\x8f\x17\x00\x82!\x93oa'