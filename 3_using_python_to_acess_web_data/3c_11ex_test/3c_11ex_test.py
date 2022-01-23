import urllib.request , urllib.error , urllib.parse
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter the URL:")
html = urllib.request.urlopen(url,context=ctx)
data = html.read().decode()
js = json.loads(data)

#print(json.dumps(js, indent=4))

sum = 0
d = js['comments']

for i in d:
    sum += i['count']

print(sum)
