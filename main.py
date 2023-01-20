#Tip calculator....
print("Welocome to the tip calculator")
bill = float(input("What was the total bill? Rs "))

percentage= int(input("what pearcntage tip of the bill would u like to pay - 10, 12, or 15 "))
people = int(input("how many people to split the bill?"))
tip = percentage / 100 * bill + bill
print(tip)

