import re
from flask import Flask, request, jsonify
import json
import api
from api import *
app = Flask(__name__)

@app.route('/api', methods=['GET'])
def run_api():
    dic=request.args.copy().to_dict()
    print(dic['fun'])
    fun=dic['fun']
    return api.__dict__[fun](dic)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
