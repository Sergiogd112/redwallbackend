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
    thread=Thread(updater(),daemon=True,name='autoupdater')
    thread.start()

    print('done')
    
    dic=request.args.copy().to_dict()
    if (dic['fun']=='search'):
        return get_top_img_urls(dic)
    else:
        return api.__dict__[dic['fun']]()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
