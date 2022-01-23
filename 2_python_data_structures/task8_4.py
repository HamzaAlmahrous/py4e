fileName = input("Enter file name: ")
fh = open(fileName)

emptylist = list()
for line in fh:
    line = line.rstrip()
    splitline = line.split()
    for element in splitline:
        if element in emptylist : continue
        emptylist.append(element)
        emptylist = sorted(emptylist)
print(emptylist)
