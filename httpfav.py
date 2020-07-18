import mmh3
import requests
import codecs

response = requests.get(input('(input) Enter the URL: '))
#If you a SSL/TLS error uncomment the below line and comment the above line, that could fix the problem
#response = requests.get(input('(input) Enter the URL: '), verify=False)
favicon = codecs.encode(response.content,"base64")
hash = mmh3.hash(favicon)
print(f"(output) Shodan-Dork: http.favicon.hash:{hash}")
