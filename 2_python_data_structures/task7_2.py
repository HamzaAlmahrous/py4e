fileName = input("Enter file name: ")
fh = open(fileName)
lineNum = 0 
sumNum = 0 
xDSPAM = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    lineNum = lineNum + 1
    xDSPAM = line[line.find('0') : ]
    xDSPAM = float(xDSPAM)
    sumNum = sumNum + xDSPAM
median = sumNum / lineNum
print("Average spam confidence:", median)