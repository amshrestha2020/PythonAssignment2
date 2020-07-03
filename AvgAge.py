'Create a list of tuples of first name, last name, and age for your friends and colleagues.'
'If you dont know the age, put in None.'
'Calculate the average age, skipping over any None values.'
'Print out each name, followed by old or young if they are above or below the average age.'


'Added one None age'
names = [("Asim", "Sherpa", 35), ("Michael", "Jackson", 20), ("Bhairab", "Giri", None)]

average_age = 0
age_counts = 0

'Calculate the average age, skipping over any None values'
for (first_name, last_name, age) in names:
    if age is not None:
        average_age = average_age + age
        age_counts = age_counts + 1

average_age = average_age / age_counts

print("The average age of a person from a list is :", average_age)

'Print out each name, followed by old or young if they are above or below the average age.'
for (first_name, last_name, age) in names:
    if age is None:
        print(first_name, last_name, "unknown")
    elif age >= average_age:
        print(first_name, last_name, "old")
    else:
        print(first_name, last_name, "young")


    # if age:
    #     lst = filter(lambda x:x[1]['age'] == None,d.items())
    # print(list(lst))

