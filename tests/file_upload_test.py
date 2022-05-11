import os
from flask_login import FlaskLoginClient
from app import config, db, User
from app.songs import csv_upload

# using the link below Flask-Login provides a simple, custom test client class that will set the user’s login cookie
# https://flask-login.readthedocs.io/en/latest/#automated-testing


def test_upload_csv_denied(application):
    """ Attempting to upload a csv file without being logged in """
    application.test_client_class = FlaskLoginClient
    # no user in session = no user logged in
    assert db.session.query(User).count() == 0
    with application.test_client(user=None) as client:
        response = client.post('/songs/upload')
        assert response.status_code == 302
        root = config.Config.BASE_DIR
        musicfile = os.path.join(root, '../music.csv')
        form = csv_upload()
        form.file = musicfile
        assert form.validate
