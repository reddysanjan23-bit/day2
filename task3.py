item_name = input("Enter the name of the item:")
item_price = float(input("Enter the price of the item:"))
number_of_people = int(input("Enter the number of people splittin the bill:"))
split_price = item_price / number_of_people
print(f"Each person should pay:{split_price:.2f}")