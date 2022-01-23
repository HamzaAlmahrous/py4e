fileName = input("Enter file name: ")
if len(fileName) < 1 : fileName = "mbox-short.txt"
fh = open(fileName)

count = 0

for line in fh:
    line = line.rstrip()
    if line.startswith('From:') :
        splitline = line.split()
        print(splitline[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")