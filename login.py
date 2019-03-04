import requests

payload = {'username':'11','password':'11'}
s = requests.session()
s.get('http://127.0.0.1:8080')
r = s.post('http://127.0.0.1:8080/login/',data = payload)
print(s.get('http://127.0.0.1:8080').content)