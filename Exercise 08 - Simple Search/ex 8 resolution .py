#list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
#search term from the user
search_term = input("Enter the name you want to search")
#Search for the term in the list
if search_term in names:
    print(f"{search_term} was found in the list.")
else:
    print(f"{search_term} was not found in  the list.")