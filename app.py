import re
from flask import Flask, request, jsonify
import json
import api
from api import *
import time
app = Flask(__name__)
import json
from threading import Thread



@app.route('/api', methods=['GET'])
def run_api():
    dic=request.args.copy().to_dict()
    with open('storeddata/status.txt','r') as f:
        status=f.read()
    with open('storeddata/data.json','r') as f:
        data=json.load(f)
    if(status=='updated'and time.gmtime(data['date']).tm_mday != time.gmtime(time.time()).tm_mday):
        print('updating')
        thread=Thread(gen_files())
        thread.start()
    return json.dumps(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
