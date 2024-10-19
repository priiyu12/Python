def interest(balance,rate,months):
	try:
		intrest=(balance*rate)/months
		return intrest
	except ZeroDivisionError:
		print("Cannot be zero months")

balance=int(input("Enter balance: "))
rate=int(input("Enter rate: "))
months=int(input("Enter months: "))
interest=interest(balance,rate,months)
print("Interest: ",interest)