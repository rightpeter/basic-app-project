import os

_ROOT = os.path.dirname(__file__)

TITLE = u"ARES"
SUB_TITLE = "ARES"
DOMAIN_NAME = "ares.qiniu.io"
HANDLERS = (
    'web',
)

LOGIN_URL = "/login/"
COOKIE_SECRET = "/hncZPV7TVaxY/krcQFc9Ujm6blLPk9Bsh6xdIYfAuc="

WEBMASTER = ''
ADMIN_EMAILS = []

DEFAULT_DATABASE_NAME = 'ares-mongo'

OAUTH_SETTINGS = {
    'client_id': '',
    'client_secret': '',
    'base_url': '',
    'redirect_url': ''
}

try:
    from local_settings import *
except ImportError:
    pass
