
#👽 defining a function

def greet(name):
    return f"good morning! {name}"


#👽 funcion with default argument
def greet(name = 'shallu'):
    return f"good morning! {name}"


print(greet())

#👽 positional vs keyword Args
def show(name, age):
    print(f"{name} is {age} years old.")

show("Shallu", 22) # positional args
show(age=22, name="Shallu")  # keyword args

#👽 *args and **kwargs
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4))  # 10

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_info(name="Shallu", age=22)

#🟨 What Are *args and **kwargs?
'''
They're used when you don’t know how many arguments will be passed to your function.

🔹 *args: Non-keyword variable-length arguments

Collects extra positional arguments (values without variable names) into a tuple
you can name it anything but the * is what matters 

🔹 **kwargs: Keyword variable-length arguments

Collects extra keyword arguments (name=value pairs) into a dictionary

This allows you to pass a variable number of arguments to a function, making it flexible and adaptable to different situations.
'''
def print_info(**kwargs):
    print(kwargs)

print_info(name="Shallu", age=20, city="Indore")

def example(a, b, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    print("args =", args)
    print("kwargs =", kwargs)

example(1, 2, 3, 4, name="Shallu", age=22)


#👽 Lambda Functions

square = lambda x: x ** 2
print(square(5))  # 25


#🍄 -----------Mini Challenge------------ 🍄

# to check a prime no 

def PrimeNo(val):
    if (val%2 != 0) :
        return f'{val} is prime no'
    else :
        return f'{val} not prime no'
    
print(PrimeNo(67))

# a func that takes list and returns a new list with only even no

li = [4,9,7,8,4,6,2,3,1]

def extract_even(li):

    even_list = []
    for i in li:
        if i % 2 == 0:
            even_list.append(i)
    return even_list

print(extract_even(li))  # Output: [4, 8, 4, 6, 2]

# sample_list = [10, 15, 22, 33, 40, 57, 88]
# result = extract_even(sample_list)
# print(result)


# a lambda function to multiply 3 numbers

mul = lambda a,b,c: a*b*c

print(mul(2, 3, 4))  # Output: 24

# a function that accepts any number of keyword arguments and returns them as a dictionary.

def collect_kwargs(**kwargs):
    return kwargs
print(collect_kwargs(name="Shallu", age=22, city="Indore"))  # Output: {'name': 'Shallu', 'age': 22, 'city': 'Indore'}