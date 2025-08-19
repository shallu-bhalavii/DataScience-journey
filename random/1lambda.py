# lambda = is an anonymous function (a function without name)
# lambda arguments: expression
# lambda can take any no of arguments but only one expression

cal = lambda num: "even number" if num%2==0 else "odd number"

print(cal(10))

string = 'what the hell'

#✔️ lambda returns a function object
print(lambda string: string)

#✔️ lambda returns a function object, we call it by passing an argument
string = 'what the hell'
print((lambda string: string)(string))

'''(lambda s: s) creates an anonymous function that returns its input.

(string) calls that lambda with 'GeeksforGeeks'.

The result gets printed.'''

#✔️ Invoke lambda function return value to peform various operations

filter_nums = lambda s: ''.join([ch for ch in s if not ch.isdigit()])
print("filter_nums():", filter_nums("Geeks101"))

do_exclaim = lambda s: s + '!'
print("do_exclaim():", do_exclaim("I am tired"))

find_sum = lambda n: sum([int(x) for x in str(n)])
print("find_sum():", find_sum(101))

'''  filter_nums(): Geeks
     do_exclaim(): I am tired!
     find_sum(): 2'''


#✔️ Difference between lambda and normal function call
'''we cannot use multiple statements inside a lambda function and allowed statements are also very limited inside lambda statements. Using lambda functions to do complex operations may affect the readability of the code'''

def cube(y):
    print(f"Finding cube of number:{y}")
    return y * y * y


lambda_cube = lambda num: num ** 3

# invoking simple function
print("invoking function defined with def keyword:")
print(cube(30))
# invoking lambda function
print("invoking lambda function:", lambda_cube(30))

'''invoking function defined with def keyword:
   Finding cube of number:30
   27000
   invoking lambda function: 27000'''   

#✔️ Lambda function with multiple arguments
'''Lambda functions can take multiple arguments, but they can only have one expression. The syntax is similar to that of a normal function, but without the def keyword.'''
# lambda arg1, arg2, ... : expression

add = lambda a, b: a + b
print(add(5, 3))  # Output: 8

#✔️ Lambda function with no arguments
'''Lambda functions can also be defined without any arguments. In this case, the function simply returns a constant value or performs an operation that does not require input.'''
# lambda : expression
greet = lambda: "Hello, Shallu!"
print(greet())  # Output: Hello, Shallu!


#✔️ The lambda function gets more helpful when used inside a function.-----------------



l = ["1", "2", "9", "0", "-1", "-2"]
# sort list[str] numerically using sorted()
# and custom sorting key using lambda
print("Sorted numerically:",
      sorted(l, key=lambda x: int(x)))

# filter positive even numbers
# using filter() and lambda function
print("Filtered positive even numbers:", 
      list(filter(lambda x: not (int(x) % 2 == 0 and int(x) > 0), l)))

# added 10 to each item after type and
# casting to int, then convert items to string again
print("Operation on each item using lambda and map()",
      list(map(lambda x: str(int(x) + 10), l)))



'''
   Sorted numerically: ['-2', '-1', '0', '1', '2', '9']
   Filtered positive even numbers: ['1', '9', '0', '-1', '-2']
   Operation on each item using lambda and map() ['11', '12', '19', '10', '9', '8']'''   


# 🐤   Time Complexity:
# The time complexity of the filter function is O(n) where n is the number of elements in the list. The lambda function does not affect the time complexity, as it is a simple check that takes constant time.

# 🐤  Space Complexity:
# The space complexity of this code is O(n) because it creates a new list that contains only odd numbers from the original list. The original list is not modified, so it remains the same size.