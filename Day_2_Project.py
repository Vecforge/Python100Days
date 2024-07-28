#-------------------------Tip Calculator---------------------------
print("Welcome to the tip calculator!")
bill_amt = float(input("What is the total bill? "))
tip_per = int(input("How much percentage of the bill would you like to give as a tip? "))
people = int(input("How many people to split the bill? "))
bill_for_each = (((tip_per/100) * bill_amt) + bill_amt) / people
print(f"Each person should pay: ${round(bill_for_each, 2)}")
