import requests
import api
topimurls=requests.get(url='http://localhost:5000/api?fun=get_top_img_urls&sub=EarthPorn&n=20&per=d')
subicon=requests.get(url='http://localhost:5000/api?fun=get_icon_sub&sub=EarthPorn')

print('urls imgs:',topimurls.text)
print('subicon url:', subicon.text)