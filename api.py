import get_top_images
import praw
import json
from threading import Thread
from multiprocessing import Pool
import time


def get_top_img_urls(dic=None, sub=None, n=100, period='d'):
    if(type(dic) == type('')):
        sub = dic
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
    submission = get_top_images.get_top_submissions(sub, n, period)
    data = [{'imgurl': x, 'score': y, 'suburl': z, 'sub': sub}
            for (x, y, z) in get_top_images.image_urls_Pool(submission)]
    return json.dumps({'response': data})


def get_icon_sub(dic=None, sub=None):
    r = praw.Reddit(user_agent='nagracks')

    if (not (sub)):
        sub = dic['sub']
    return json.dumps({'url': r.get_subreddit(sub).icon_img})


def get_cured(dic=None, subs=None, n=20, per='d'):
    if (not (subs)):
        subs = dic['subs'].split('-')
        try:
            n = int(dic['n'])
        except:
            pass
        try:
            per = dic['per']
        except:
            pass
    data = []

    for sub in subs:
        data += json.loads(get_top_img_urls(sub=sub,
                                            n=n, period=per))['response']
    data2 = sorted(data, key=lambda l: l['score'])[::-1]
    return json.dumps(data2)


def gen_files(path='storeddata/data.json', subs=['EarthPorn', 'MinimalWallpaper', 'Wallpaper', 'phonewallpapers', 'iWallpaper', 'wallpaperdump', 'spaceporn']):
    print(subs)
    with open('storeddata/status.txt','w') as f:
        f.write('updating')
    # ---- gen category ----
    print('Categories')
    # day
    print('day')
    day_data = [json.loads(get_top_img_urls(sub, period='d'))['response'] for sub in subs]
    day_cat = dict(zip(subs, day_data))
    # week
    print('week')
    week_data = [json.loads(get_top_img_urls(sub, period='w'))['response'] for sub in subs]
    week_cat = dict(zip(subs, week_data))
    # month
    print('month')
    month_data = [json.loads(get_top_img_urls(sub, period='m'))['response'] for sub in subs]
    month_cat = dict(zip(subs, month_data))
    # year
    print('year')
    year_data = [json.loads(get_top_img_urls(sub, period='y'))['response'] for sub in subs]
    year_cat = dict(zip(subs, year_data))
    # all
    print('all')
    all_data = [json.loads(get_top_img_urls(sub, period='a'))['response'] for sub in subs]
    all_cat = dict(zip(subs, all_data))
    # ---- gen curated ----
    print('curated')
    # day
    print('day')
    day_cured = sorted([sub for subs in day_data for sub in subs], key=(lambda l: int(l['score'])))[::-1]
    # week
    print('week')
    week_cured = sorted([sub for subs in week_data for sub in subs], key=(lambda l: int(l['score'])))[::-1]
    # month
    print('month')
    month_cured = sorted([sub for subs in month_data for sub in subs], key=(lambda l: int(l['score'])))[::-1]
    # year
    print('year')
    year_cured = sorted([sub for subs in year_data for sub in subs], key=(lambda l: int(l['score'])))[::-1]
    # all
    print('all')
    all_cured = sorted([sub for subs in all_data for sub in subs], key=(lambda l: int(l['score'])))[::-1]
    # ---- gen icons ----
    print('icons')
    icons = dict([[sub, get_icon_sub(sub=sub)] for sub in subs])
    data = {
        'cat': {
            'day': day_cat,
            'week': week_cat,
            'month': month_cat,
            'year': year_cat,
            'all': all_cat
        },
        'cured': {
            'day': day_cured,
            'week': week_cured,
            'month': month_cured,
            'year': year_cured,
            'all': all_cured
        },
        'icons': icons,
        'date': time.time()
    }
    json.dump(data,open('storeddata/data.json','w'))
    with open('stored/status.txt','w') as f:
        f.write('updated')

if __name__ == '__main__':
    gen_files()
    print()
