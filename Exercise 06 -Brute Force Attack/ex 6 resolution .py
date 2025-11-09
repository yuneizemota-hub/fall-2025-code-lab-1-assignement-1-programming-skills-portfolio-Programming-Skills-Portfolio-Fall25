correct_password = "12345"
max_attempts = 5
attempts = 0
#keep asking for the password until correct 
while attempts < max_attempts:
     user_input = input("Enter the password: ")
     if user_input == correct_password:
       print("Authorized")
       break  # Exit the loop if the password is correct
     else: 
         attempts += 1
         remaining_attempts = max_attempts - attempts
         if remaining_attempts > 0:
          print(f"Incorrect password. You have {remaining_attempts} attempts left.")
         else:
          print("Incorrect password. No attempts left.")
# If the loop finishes all attempts used)
if attempts == max_attempts:
    print("Maximum attempts reached")
