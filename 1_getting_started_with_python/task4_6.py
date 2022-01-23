hours = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
def computepay(hours,rate) :
    if hours > 40 :
        return 40 * rate + (hours-40)*1.5*rate
    elif hours < 0 :
        print("Entered hours is wrong")
    else :
        return hours * rate
pay = computepay(hours, rate)
print("Pay",pay)