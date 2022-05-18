import sys
import requests                       #웹페이지 연결
from bs4 import BeautifulSoup as bs   #가져온 페이지를 분석하기 용이하게 정제
# import pandas as pd  
from datetime import datetime, timedelta, timezone


### ONEJAV ###

ppv_list = []
rank = 1

# datetime_utc = datetime.utcnow()
# timezone_kst = timezone(timedelta(hours=9))
# datetime_kst = datetime_utc.astimezone(timezone_kst).strftime("%Y-%m-%d %H:%M:%S")
# print(datetime_kst)


html = requests.get('https://onejav.com/search/PPV?page=1')
soup = bs(html.text)

ppvs = soup.select('div.card.mb-3')

for ppv in ppvs:
  title = ppv.select('h5.is-spaced > a')[0].text.strip()
  date = ppv.select('p.is-6 > a')[0].text.strip()
  ppv_list.append(['onejav','FC2- '+title, date])
  rank += 1

# html = requests.get('https://onejav.com/search/PPV?page=2')
# soup = bs(html.text,"html.parser")
# ppvs = soup.select('div.card.mb-3')

# for ppv in ppvs:
#   title = ppv.select('h5.is-spaced > a')[0].text.strip()[8:] 
#   date = ppv.select('p.is-6 > a')[0].text.strip()[0:6]
#   ppv_list.append(['onejav','FC2- '+title, date])
#   rank += 1

# html = requests.get('https://onejav.com/search/PPV?page=3')
# soup = bs(html.text,"html.parser")
# ppvs = soup.select('div.card.mb-3')

# for ppv in ppvs:
#   title = ppv.select('h5.is-spaced > a')[0].text.strip()[8:] 
#   date = ppv.select('p.is-6 > a')[0].text.strip()[0:6]
#   ppv_list.append(['onejav','FC2- '+title, date])
#   rank += 1

ppv_list

# df.to_excel('onejav.xlsx',index=False)