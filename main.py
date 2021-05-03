height = int(input("What is your height? "))
bill = 0

if height > 120:
  age = int(input("What is your age? "))
  if age > 44 and age < 56:
    print("You do not have to pay.")
  elif age < 12:
    bill += 5
  elif age < 19:
    bill += 7
  else:
    bill += 12
    photo = input("Do you want to have a photo? ")
    if photo in("Y", "y"):
      bill += 3
    print(f"Your total bill is {bill}.")
else:
  print("You have to grow!")
