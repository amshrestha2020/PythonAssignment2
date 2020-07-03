'Create a list with the names of friends and colleagues.'
'Search for the name John using a for loop. Print not-found if you did not find it.'

'asks the user to enter their friends and colleagues name and stores it in a variable called name'
print("*******Enter name in lower or upper case*********")
name_list = [input("Enter the names of your friends and colleague(separated with comma) :")]
print("List out all the names :", name_list)
print("Search the name John from the list")

for name in name_list:
    'checks if the name variable has John stored in it '
    if ('john' in name):
         'displays Found if the condition is True'
         print("Found")
    elif ('John' in name):
        print("Found")
    elif ('JOHN' in name):
        print("Found")
    else:
         'displays Not Found if the condition does not match'
         print("Not Found")
