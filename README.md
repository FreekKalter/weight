# files/dirs to create before running service

## nginx ssl certificates

- nginx/certificates/fullchain.pem
- nginx/certificates/privkey.pem
- *when youre using letsencrypt:* nginx/letsencrypt-webroot/.well-known

## data dir (file optional)
data/(weight.db)

## python webapp config file
webapp/instance/flask.cfg

### example flask.cfg
    import os


    # grab the folder of the top-level directory of this project
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    TOP_LEVEL_DIR = os.path.abspath(os.curdir)

    # Update later by using a random number generator and moving
    # the actual key outside of the source code under version control
    SECRET_KEY = b'\xd6gRP\xe6\xe9k\x94\xe3\xed\xf3\xa9\x7f!R\xe2J.\x88S-\xd2\x0b\xc9'
    DEBUG = True
