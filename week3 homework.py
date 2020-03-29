import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200327',headers=headers)



soup = BeautifulSoup(data.text, 'html.parser')
rows = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
rank =1



for row in rows :

    music_name = row.select_one('td.info > a.title.ellipsis')
    if music_name != None:
        artist = row.select_one('a.artist.ellipsis').text

        music_name = music_name.text.strip()

        print(rank,music_name,artist)

        rank += 1