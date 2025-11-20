# Dictionary in which month numbers are the keys and days are the values
days_in_month ={
1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
# month number from the user
month = int(input("Enter the month number (1-12): "))
#Make sure the input is valid then print given days
if 1 <= month <= 12:
    print(f"The number of days in month {month} is {days_in_month[month]}.")
else:
    print("Invalid month number.Enter a number between 1 and 12.")