# def is_even(nums):
#     """Return a list of even numbers from the given list."""
#     return [num for num in nums if num % 2 == 0]

# print(is_even([1, 2, 3, 4, 5, 6]))  # Output: [2, 4, 6]
# print(is_even.__doc__)  # Output: Return a list of even numbers from the given list.


# #diiferent ways to pass arguments to function
# def greet(name, greeting="Hello"):
#     """Greet a person with the given greeting."""
#     return f"{greeting}, {name}!"
# print(greet("Alice"))  # Output: Hello, Alice!
# print(greet("Bob", "Hi"))  # Output: Hi, Bob!
# print(greet.__doc__)  # Output: Greet a person with the given greeting.

# def sum_numbers(*args):
#     """Return the sum of all the numbers passed as arguments."""
#     return sum(args)
# print(sum_numbers(1, 2, 3))  # Output: 6
# print(sum_numbers(4, 5))  # Output: 9

# def print_info(**kwargs):
#     """Print the information passed as keyword arguments."""
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print_info(name="Alice", age=30, city="New York")
# # Output:
# # name: Alice
# # age: 30
# # city: New York

# #postional arguments,keyword arguments,default arguments,variable length arguments

# def calculate_area(radius, pi=3.14):
#     """Calculate the area of a circle given its radius."""
#     return pi * radius ** 2
# print(calculate_area(5))  # Output: 78.5
# print(calculate_area(5, 3.14159))  # Output: 78

# def factorial(n):
#     """Return the factorial of a number."""
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))  # Output: 120

# def flexi(*args, **kwargs):
#     """Demonstrate the use of *args and **kwargs."""
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)
# flexi(1, 2, 3, name="Alice", age=30)
# # Output:
# # Positional arguments: (1, 2, 3)
# # Keyword arguments: {'name': 'Alice', 'age': 30}

# #in pythin everything is object including functions
# def sample_function():
#     pass
# print(type(sample_function))  # Output: <class 'function'>
# print(dir(sample_function))  # Output: List of attributes and methods of the function object
# print(sample_function.__doc__)  # Output: None


#pass fucntion as argument to another function
def apply_function(func, value):
    """Apply a function to a given value."""
    return func(value)
def square(x):
    """Return the square of a number."""
    return x * x
print(apply_function(square, 5))  # Output: 25
print(apply_function(lambda x: x + 10, 5))  # Output: 15


