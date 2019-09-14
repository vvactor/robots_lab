import requests
import re
# from html.parser import HTMLParser

def lyric_filter(lyric):
    temp = re.sub(r'\[(.*?)\]', '', lyric.replace('&', '').replace('#', '').replace(';', ' '))
    return re.sub(r'\d+', '', temp)

song_url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
song_headers = {
    'origin':'https://y.qq.com',
    'referer':'https://y.qq.com/portal/search.html',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
count = 1
for page in range(1, 6):
    song_params = {
    'ct': '24',
    'qqmusic_ver': '1298',
    'new_json': '1',
    'remoteplace': 'txt.yqq.song',
    'searchid': '62440814424449801',
    't': '0',
    'aggr': '1',
    'cr': '1',
    'catZhida': '1',
    'lossless': '0',
    'flag_qc': '0',
    'p': str(page),
    'n': '10',
    'w': '周杰伦',
    'g_tk': '5381',
    'loginUin': '0',
    'hostUin': '0',
    'format': 'json',
    'inCharset': 'utf8',
    'outCharset': 'utf-8',
    'notice': '0',
    'platform': 'yqq.json',
    'needNewCode': '0'
    }
    song_list = requests.get(song_url, headers=song_headers, params=song_params).json()
    song_list_per_page = song_list['data']['song']['list']
    lyric_url = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
    for song in song_list_per_page:
        musicid = song['id']
        name = song['name']
        mid = song['mid']
        lyric_headers = {
        'origin':'https://y.qq.com',
        'referer':'https://y.qq.com/n/yqq/song/' + mid + '.html',
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        lyric_params = {
            'nobase64': '1',
            'musicid': musicid,
            '-': 'jsonp1',
            'g_tk': '5381',
            'loginUin': '0',
            'hostUin': '0',
            'format': 'json',
            'inCharset': 'utf8',
            'outCharset': 'utf-8',
            'notice': '0',
            'platform': 'yqq.json',
            'needNewCode': '0'
        }
        res_lyric = requests.get(lyric_url, headers=lyric_headers, params=lyric_params).json()
        lyric = res_lyric['lyric']
        lyric = lyric_filter(lyric)
        print('No.%d —— 歌曲《%s》的歌词：\n%s' %(count, name, lyric))
        print('-----------------------------------------------------------')
        count += 1