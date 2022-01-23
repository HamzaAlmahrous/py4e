import re
fname = input("Enter the file name :")
fhead = open(fname,'r')
x = fhead.read()
l = re.findall('[0-9]+',x)
sum = 0
for i in range(0, len(l)):
    sum += int(l[i])
print(sum)
