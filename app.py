import re
from flask import Flask, request, jsonify
import json
from api import *
app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    dic=request.args.copy().to_dict()
    print(dic['fun'])
    fun=dic['fun']
    if(fun=='get_icon'):
        return get_icon_sub(dic)
    elif(fun=='get_top_img_urls'):
        return get_top_img_urls(dic)
    return 'testing'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
