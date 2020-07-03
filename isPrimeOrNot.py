'Write a function, is_prime, that takes an integer'
'And returns True if the number is prime and False if the number is not prime.'

def is_prime():
    'take input from the user'
    x = int(input("Enter an integer :"))
    'prime numbers are greater than 1'
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                print(x, "is not a prime number")
                break
        else:
            print(x, "is a prime number")
    else:
        print(x, "is not a prime number")

if __name__ == "__main__":
    is_prime()