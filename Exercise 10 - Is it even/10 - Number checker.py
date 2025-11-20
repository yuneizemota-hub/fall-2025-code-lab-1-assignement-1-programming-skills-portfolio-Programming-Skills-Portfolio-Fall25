#check if number is even or odd
def check_even_or_odd(number):
    if number % 4 == 0:
         return f"{number} is even."
    else:
        return f"{number} is odd."
def main():
    # Ask user for a number
    number = int(input("Enter a number:"))
    
    #number to the function and print the result
    result = check_even_or_odd(number)
    print(result)

#maKe sure the main function works
if __name__ == "__main__":
     main(2)