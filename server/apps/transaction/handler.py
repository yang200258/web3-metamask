import json
from web3 import Web3

from apps.transaction.models import User
from web3_backend.handler import BaseHandler
from web3_backend.settings import api_key
from web3.middleware import geth_poa_middleware


class TransferHandler(BaseHandler):
    async def post(self):
        try:
            provider = Web3.HTTPProvider("https://eth-goerli.alchemyapi.io/v2/" + api_key)
            web3 = Web3(provider)
            web3.middleware_onion.inject(geth_poa_middleware, layer=0)
            param = self.request.body.decode("utf8")
            param = json.loads(param)
            res = web3.eth.wait_for_transaction_receipt(param['transactionHash'])
        except Exception as e:
            self.set_status(400);
            self.finish({'success': False, 'msg': e})
        self.set_status(200)
        self.finish(web3.toJSON(res))
