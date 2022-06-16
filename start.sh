#!/bin/bash
cd client
npm i
npm run build
# mv ./dist/ /home/deploy/web3_client/
cd ../server
pip install -r requirements.txt
nohup python server.py