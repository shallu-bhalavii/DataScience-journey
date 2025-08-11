# ----------------------- 6-08-2025------------------------
''' 🐤take user input
    🐤prints whether they are eligible to vote(18+)
    🐤includes a greet(name) function'''

while True:
    def greetname():
            name = input("enter your name: ").lower().strip()
            age  = int(input("enter your age: "))

            if (age>=18):
                print(f'hello {name}! \n{age}, you are eligible to vote!!')
            else:
                print(f'hello {name}! \n{age}, you are not eligible to vote!!')


    greetname()

