import re  # Search and manipulate strings
import os  # I/O
import requests  # Make HTTP requests
from bs4 import BeautifulSoup  # Scrape data from an HTML document

# def scrape_song_lyrics(url) =>  Scrape lyrics from a Genius.com song URL
# def write_lyrics_to_file(artist_name, song_count)  =>  Loop through all URL’s and write lyrics to one file

# my account key
GENIUS_API_TOKEN = '95N_UrNaiFgPcGn_IdlVO1MX7Y-Fn4tpLKLWVmJMGh0h06T1teuNhqZkcSiAsbvn'

# Error !!! AttributeError: 'NoneType' object has no attribute 'get_text' => 注意前面空格，馬的


def scrape_song_lyrics(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyric = html.find("div", class_='lyrics').get_text()
    lyric = re.sub(r'[\(\[].*?[\)\]]', '', lyric)  # remove identifiers like chorus, verse, etc
    lyric = os.linesep.join([s for s in lyric.splitlines() if s]) # remove empty lines
    return lyric


def write_lyrics_to_file(url, singer, song):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyric = html.find('div', class_='lyrics').get_text()
    f = open((singer + ' ' + song).lower() + '.txt', 'wb+')
    f.write(lyric.encode("utf8"))
    f.close()


print("請問要查哪位歌手的歌曲 : ", end='')
singer = input(str())
print("請問要找" + singer + "的哪首歌曲 : ", end='')
song = input(str())
search = singer + ' ' + song
searchflie = search.lower()
search = search.replace(' ', '-')
print("\n即將顯示出歌詞 . . . 請稍等 . . .\n")
print(scrape_song_lyrics('https://genius.com/' + search + '-lyrics'))
print('\n\n')
url = 'https://genius.com/' + search + '-lyrics'

filepath = "C:/Users/陳鼎元/Desktop/Python_scrapy/" + searchflie + '.txt'
if os.path.isfile(filepath):
    print("此歌詞檔已經存過了哦 ~~~")
else:
    print("歌詞檔不存在")
    print("\n想要將此歌手的歌詞存檔嗎???  回應(好或不要) : ", end='')
    write = input(str())
    if (write == "好"):
        write_lyrics_to_file(url, singer, song)
        print("\n恭喜 !!! 此歌詞已經存好囉 !!!")



