'Write a function that reads a CSV file.'
'It should return a list of dictionaries, using the first row as key names, and each subsequent row as values for those keys.'

'For the data in the previous example it would return:'
"""[{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, 
    {'name': 'John', 'address': '54 Love Ave', 'age': 21}]"""

import csv

filename = "test.txt"
accessMode = "r"

'Function for reading .csv file'
def csv_reader():
    with open(filename, accessMode) as myCSVFile:
        'read the file contents'
        'specify that we are using a comma to separate the values in the file'
        dataFromFile = csv.reader(myCSVFile, delimiter ="," )

        for row in dataFromFile:
            'print an entire row at a time in a list format'
            print(row)

            # 'print the entire row separating the values in the list'
            # print(', '.join(row))

    myCSVFile.close()

if __name__ == "__main__":
    csv_reader()

