'Create a function, is_Palindrome, to determine if a supplied word is the same if the letters are reversed.'

def main():
    is_Palindrome()

def is_Palindrome():
    string = input("Enter the string: ")
    reverse_string = string[::-1]
    print("reversed string: ", reverse_string)
    if string == reverse_string:
        print("String is palindrome.")
    else:
        print("String is not palindrome.")

if __name__ == "__main__":
    main()