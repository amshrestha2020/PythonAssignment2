'Write a function to write a comma-separated value (CSV) file.'
'It should accept a filename and a list of tuples as parameters.'
'The tuples should have a name, address, and age.'
'The file should create a header row followed by a row for each tuple.'
'If the following list of tuples was passed in:'

""""[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]"""

'it should write the following in the file:'
'name,address,age'
'George,4312 Abbey Road,22'
'John,54 Love Ave,21'

# filename = 'data.csv'
# data = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]

def csv_writer(filename, data):
    """write a file with name passed in and tuples as lines"""
    with open(filename, 'w') as fout:
        fout.write("'name', 'address', 'age' \n")

        for info in data:
            fout.write(f"'{info[0]}','{info[1]}','{info[2]}'\n")

filename = 'data.csv'
data = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
csv_writer(filename, data)

