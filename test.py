import requests
import api

api.get_top_img_urls(sub='EathPorn',n=100,period='d')
import praw

r = praw.Reddit(user_agent='nagracks')
all_submissions=r.get_subreddit('EarthPorn',fetch=True)
timeframe = {
        'h': all_submissions.get_top_from_hour,
        'd': all_submissions.get_top_from_day,
        'w': all_submissions.get_top_from_week,
        'm': all_submissions.get_top_from_month,
        'y': all_submissions.get_top_from_year,
        'a': all_submissions.get_top_from_all
        }
submissions=timeframe.get('d')(limit=100)
# print([sub.upvotes for sub in submissions])
print([sub.score for sub in submissions])