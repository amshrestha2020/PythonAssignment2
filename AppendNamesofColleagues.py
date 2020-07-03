'Create a list.'
'Append the names of your colleagues and friends to it.'
'Has the id of the list changed? Sort the list. What is the first item on the list? What is the second item on the list?'

names = []

print("List ID :", id(names))
names.append("John")
names.append("Albert")
print("List ID :", id(names))
names.sort()
print("First item on list :", names[0])
print("Second item on list :", names[1])

