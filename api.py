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
    submission = get_top_images.get_top_submissions(sub, n, period)
    data = [x for x in get_top_images.image_urls(submission)]
    return json.dumps({'response': data})


def get_icon_sub(dic=None, sub=None):
    r = praw.Reddit(user_agent='nagracks')

    if(not(sub)):
        sub = dic['sub']
    print('get icon:', sub)
    return json.dumps({'url': r.get_subreddit(sub).icon_img})


if __name__ == '__main__':
    print(get_top_img_urls(sub='EarthPorn', n=20, period='d'))
