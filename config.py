import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'super-secret'

OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '781375168673603',
        'secret': 'a43099723dc1c00787ac70af1c545eec'
    }
}