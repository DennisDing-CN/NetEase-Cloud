import requests
import execjs

with open('2.js', 'r', encoding='utf8') as f:
    line = f.read()

par = execjs.compile(line).call('jiami', 1895164923)
# print(par)
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
}
data={
    'params': par['encText'],
    'encSecKey': par['encSecKey'],
}
# print(data)
# proxies = {
# 			"https": "http://127.0.0.1:8888",
#      	 }
response = requests.post('https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=', headers=headers, data=data)
print(response.text)
# url = response['data'][0]['url']
# with open('3.mp3', 'wb') as f:
#     f.write(requests.get(url).content)
