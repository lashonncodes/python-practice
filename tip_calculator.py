print("Welcome to the Tip Calculator")

# ask for bill
bill = float(input("What was the total bill? "))

# ask for tip
tip = int(input("What percentage tip would you like to give? "))

# how many people
people = int(input("How many people to split the bill? "))

print(bill)
print(tip)
print(people)

per_person = (bill * (1 + tip / 100)) / people
print(per_person)

final_amount = round(per_person, 2)
print(final_amount)

print(f"Each person should pay ${final_amount}.")
