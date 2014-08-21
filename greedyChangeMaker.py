import math
class greedyChangeMaker:
	penny = 0.01
	nickel = 0.05
	dime = 0.10
	quarter = 0.25
	half_dollar = 0.50
	coins = ["Pennies: ", "Nickels:", "Dimes: ", "Quarters: ", "Half_dollars: "]
	total = input("Enter the amount you want to make change for or 0 to exit: ")
	amount = total
	while total != 0:
		#makes change with the biggest coins first, then goes to small ones
		if math.floor(total/half_dollar) != 0:
			coins[4] = "Half Dollars: " + str(int(math.floor(total/half_dollar)))
			total = total - math.floor(total/half_dollar) * 0.50
		if math.floor(total/quarter) != 0:
			coins[3] = "Quarters: " + str(int(math.floor(total/quarter)))
			total = total - math.floor(total/half_dollar) * 0.25
		if math.floor(total/dime) != 0:
			coins[2] = "Dimes: " + str(int(math.floor(total/dime)))
			total = total - math.floor(total/dime) * 0.10
		if math.floor(total/nickel) != 0:
			coins[1] = "Nickels: " + str(int(math.floor(total/nickel)))
			total = total - math.floor(total/nickel) * 0.05
		coins[0] = "Pennies: " + str(int(total/penny))
		print("The change for " + str(amount) + " dollars is the following: ")
		for i in range(len(coins)):
			print coins[i]
		#keeps the loop going while total != 0
		total = input("\nEnter the amount you want to make change for or 0 to exit: ")
		amount = total
	if total == 0:
		print("\nThanks for using the greedyChangeMaker! Good bye!")
