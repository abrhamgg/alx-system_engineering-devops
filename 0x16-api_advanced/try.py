import requests


data = requests.get('http://www.reddit.com/r/programming/about.json', headers={'User-Agent': "subscribers"})

print(data.json())
print((data.json().get('data')).get('subscribers'))