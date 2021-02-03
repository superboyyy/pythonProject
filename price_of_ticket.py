num_of_people = int(input("Please enter the number of people: "))

price = 0
num = 1
sum = 0

while num <= num_of_people:
    name = input("\nPlease enter your name: ")
    age = int(input("Please enter your age: "))

    if age < 0:
        print("\nThe age is invalid.")
        break
    if age < 3 / age > 60:
        price = 0
    elif 3 <= age < 12:
        price = 10
    elif 12 <= age < 18:
        price = 15
    else:
        price = 20

    print(f'\nWelcome {name}! The price of your ticket is: ${price}')

    sum += price
    num += num

print(f"\nThe total price is ${sum}")



