import get_top_images
import praw
import json


def get_top_img_urls(dic=None, sub=None, n=1, period='d'):
    if (not (sub)):
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
    data = [[x, y, z, sub] for (x, y, z) in get_top_images.image_urls(submission)]
    return json.dumps({'response': data})


def get_icon_sub(dic=None, sub=None):
    r = praw.Reddit(user_agent='nagracks')

    if (not (sub)):
        sub = dic['sub']
    print('get icon:', sub)
    return json.dumps({'url': r.get_subreddit(sub).icon_img})


def get_cured(dic=None, subs=None, n=20, per='d'):
    if (not (subs)):
        subs = dic['subs'].split('-')
        try:
            n = dic['n']
        except:
            pass
        try:
            per = dic['per']
        except:
            pass
    data = []

    for sub in subs:
        data += json.loads(get_top_img_urls(sub=sub, n=n, period=per))['response']
    data2 = sorted(data, key=lambda l: l[1])[::-1]
    return json.dumps(data2)


if __name__ == '__main__':
    (get_top_img_urls(sub='EarthPorn', n=20, period='d'))
    get_cured_(subs=['EarthPorn', 'Wallpaper', 'MinimalWallpaper','phonewallpapers'])
