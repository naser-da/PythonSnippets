import string, random

def generate(length):
    password =''

    for i in range(length):
        x = random.randint(0,95)
        password+= string.printable[x]

    return password

length = int(input("Enter the desired password length: \n"))
print(generate(length))