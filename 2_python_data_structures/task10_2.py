fileName = input("Enter file:")
if len(fileName) < 1 : fileName = "mbox-short.txt"
handle = open(fileName)

counts = dict()

for line in handle :
    if line.find ('From ') : continue
    line = line.split()
    line = line[5]
    line = line.split(':')
    line = line[0]
    counts[line] =  counts.get(line, 0) + 1#Hystagramm growth by 1 block

print("counts unsorted", counts)# hystagramm result unsorted

counts = sorted(counts.items())

print("counts sorted", counts)# hystagramm result sorted by str

for hours, times in counts:
    print(hours,times)