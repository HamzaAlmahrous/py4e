import xml.etree.ElementTree as ET
import urllib.request , urllib.error , urllib.parse
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter the URL:")
html = urllib.request.urlopen(url,context=ctx).read()

tree = ET.fromstring(html)
counts = tree.findall('comments/comment')
sum = 0
print('Count:',len(counts))
#print(counts)
for i in counts:
    #print('count', i.find('count').text)
    sum += int(i.find('count').text)

print(sum)
