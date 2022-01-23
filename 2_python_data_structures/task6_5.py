text = "X-DSPAM-Confidence:    0.8475";
firstDigit = text.find('0')
lastDigit = text.find('5') + 1
number = text[firstDigit : lastDigit]
numberfloat = float(number)
print(numberfloat)