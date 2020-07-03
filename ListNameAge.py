'Create a tuple with your first name, last name, and age.'
'Create a list, people, and append your tuple to it.'
'Make more tuples with the corresponding information from your friends and append them to the list.'
'Sort the list.'
'When you learn about sort method, you can use the key parameter to sort by any field in the tuple, firstname, lastname, or age.'


x = ("Roshin", "Shakya", 30)
people = [x]
people.append(("First Name", "Last Name", 99))
people.sort()
print(people)

