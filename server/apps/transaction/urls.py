from tornado.web import url

from apps.transaction.handler import TransferHandler

url_pattern = (
    url('/rest/transfer', TransferHandler),
)
