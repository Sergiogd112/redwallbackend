import get_top_images
import re
from flask import Flask,request,jsonify
import json


app = Flask(__name__);

@app.route('/api',methods=['GET'])
def get_top_im_urls():
    sub = request.args.get('sub')
    n = int(request.args.get('n'))
    period = request.args.get('per')
    print(sub,n,period)
    submission=get_top_images.get_top_submissions(sub,n,period)
    urls=[x for x in get_top_images.image_urls(submission)]
    return json.dumps({'response':urls})

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=80)
    