import os

# import peewee_async

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
api_key = 't0OytI-Gkt-wUXTVJXMthetJq58EQPWL'
settings = {
    "secret_key": "ZGGA#Mp4yL4w5CDu",
    "jwt_expire": 7*24*3600,
    "static_path": os.path.join(os.path.dirname(__file__), "../static"),
    "template_path": os.path.join(os.path.dirname(__file__), "../static"),
    "static_url_prefix": "/static/",
    # "redis": {
    #     "host": "127.0.0.1",
    # },
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    "login_url": "/login",
    "db": {
        "host": "127.0.0.1",
        "user": "root",
        "password": "Yy141025",
        "name": "blog",
    }
}

# database = peewee_async.MySQLDatabase(
#     'blog', host="127.0.0.1", port=3306, user="root", password="Yy141025"
# )
