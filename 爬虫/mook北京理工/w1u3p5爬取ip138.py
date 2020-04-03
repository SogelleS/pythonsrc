import requests

url = 'https://www.ip138.com/iplookup.asp?ip='

r = requests.get(url+'114.114.114.114')
print(r.text)