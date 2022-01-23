import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
          <user x="2">
                <id>001</id>
                <name>Chuck</name>
          </user>
          <user x="7">
                <id>009</id>
                <name>Brent</name>
          </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
#we make the xml file as a tree object to make it easier to read
lst = stuff.findall('users/user')
#this method (findall) return a list and ('users/user') this help to search inside users of all the user
print('User count:',len(lst))
print(lst)
for item in lst:
    print('Name', item.find('name').text)
    #this find the name field and print what is inside it which we call it the text
    print('Id:', item.find('id').text)
    print('Attribute',item.get("x"))
