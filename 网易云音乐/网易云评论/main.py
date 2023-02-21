import requests
import execjs

with open('lyrics.js', 'r', encoding='utf-8')  as f:
    line = f.read()

music_id = 1970421414
huoqu = execjs.compile(line).call('get_form', music_id)

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
data = {
    'params': huoqu['encText'],
    'encSecKey': huoqu['encSecKey']
}

url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
response = requests.post(url, headers=headers, data=data)
print(response)
print(response.text)
