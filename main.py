#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇

#Welcome message
print("Welcome to the tip calculator.")
#Total bill definition
bill = input("What was the total bill? $ ")
bill = float(bill)
#Percentage definition
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
percentage1 = ("1." + percentage)
percentage1 = float(percentage1)
#Participants definition
people = input("How many people to split the bill? ")
people = int(people)
#Calculation result and decimal conversion
result = (bill / people) * percentage1
result = ("%.2f" % result)
#Result output
print("Each person should pay: $ " + (result))
