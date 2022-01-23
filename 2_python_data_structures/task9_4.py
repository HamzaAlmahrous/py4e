fileName = input("Enter file:")
if len(fileName) < 1 : fileName = "mbox-short.txt"
handle = open(fileName)

counts = dict()

for line in handle :
    if line.find ('From ') : continue
    line = line.split()
    mails = line[1]
    counts[mails] = counts.get(mails, 0) + 1
    print("mails", mails)

mostmails = None
prolificomitter = None

for sender,amount in counts.items():
    if mostmails is None or amount > mostmails:
        print("sender, amount", sender, amount)
        mostmails = amount
        prolificomitter = sender

print(prolificomitter, mostmails)