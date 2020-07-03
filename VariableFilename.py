'Create a variable, filename'
'Assuming that it has a three-letter extension, and using slice operations, find the extension.'
'i. For README.txt, the extension should be txt.'
'ii. Write code using slice operations that will give the name without the extension.'
'Does your code work on filenames of arbitrary length?'


def filename(filename):
    return filename[:-4]

def extension(filename):
    return filename[-3:]

fullname = "README.txt"

print("Fullname of given file(README.txt) :",fullname)
print("Given filename(README.txt) without extension :",filename(fullname))
print("Given filename(README.txt) only extension :",extension(fullname))
