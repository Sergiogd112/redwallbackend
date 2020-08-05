import get_top_images
import praw
import json


def get_top_img_urls(dic=None, sub=None, n=1, period='d'):
    if(not(sub)):
        sub = dic['sub']
        try:
            n = int(dic['n'])
        except:
            pass
        try:
            period = dic['per']
        except:
            pass
    print(sub, n, period)
    submission,scores = get_top_images.get_top_submissions(sub, n, period)
    print(submission)
    urls = [(x,y) for x,y in zip(get_top_images.image_urls(submission),scores)]
    return json.dumps({'response': urls})


def get_icon_sub(dic=None, sub=None):
    r = praw.Reddit(user_agent='nagracks')

    if(not(sub)):
        sub = dic['sub']
    print('get icon:', sub)
    return json.dumps({'url': r.get_subreddit(sub).icon_img})
