print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = bill * (1 +  tip / 100)
bill_per_person = bill_with_tip / people
final_bill_person = round(bill_per_person, 2)
final_bill_person = "{:.2f}".format(bill_per_person)
print(f"Each person should pay $ {final_bill_person}")