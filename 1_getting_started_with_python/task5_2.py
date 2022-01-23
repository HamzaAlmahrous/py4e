maxNum = None
minNum = None
while True:
    num = input("Enter a number: ")
    if num == 'done' :
        break
    try:
        numint = int(num)
        if minNum is None :
            minNum = numint
        elif numint < minNum :
            minNum = numint
        if maxNum is None :
            maxNum = numint
        elif numint > maxNum :
            maxNum = numint
    except:
         print("Invalid input")
    continue

print("Maximum is", maxNum)
print("Minimum is", minNum)