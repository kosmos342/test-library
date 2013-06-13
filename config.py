import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

ADMINS = frozenset(['kosmos342@gmail.com'])
SECRET_KEY = '*\x8c3\xab\xacN:W\x88x\xc0}\xe4\xc5\xc2E\x8f\x17\x00\x82!\x93oa'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 4

CSRF_ENABLED = True
CSRF_SESSION_KEY = 'bcd4621d373cade4e832627b4f6'
