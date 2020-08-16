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


    print('done')
    
    dic=request.args.copy().to_dict()
    if (dic['fun']=='search'):
        return get_top_img_urls(dic)
    else:
        return api.__dict__[dic['fun']]()


print('started')
gen_files()
updater=Updater()
thread=Thread(target=updater.run)
thread.start()
app.run(host='0.0.0.0',debug=False)
updater.stop()
print('ended')
