hours = input("Enter Hours:")
h = float(hours)
rate = input("Enter Rate:")
r = float(rate)
if h > 40 :
    pay = 40 * r + (h-40)*1.5*r
else :
    pay = h * r
print(pay)