#Data Types
# Complex : Complex numbers are a combination of real and imaginary numbers.
# The real part can be expressed by an integer or decimal
# ,while the imaginary part has a square that is negative
# Thus j = sqrt(-1) . sqrt(-9) = +-3j.
z = 2 + 3j
print(type(z))  # Output: <class 'complex'>
print(z)
# Integers ( numbers without decimal )
x = 123
print(x)
y = 123_456_789  # helps visualize the numbers
print(y)
# Floats
dec = 1.23
print(dec)
# Booleans
is_student = True
print(is_student)
# Strings
string1 = "Hello"  # string type
# Sub Strings : slices of strings
# Indexing : selecting a character in a string
print(string1[0])  # character of a string can be taken - sub string
print(string1[-1]) # last element
print(string1[0:2])  # slice of a string, the end index is not included
print(string1[:2])  # slice of a string , from start
print(string1[2:])  # slice of a string , till end, the start index is included
print(string1[::2])  # slice of a string , every other character as 2
print(string1[::3])  # slie of a string , every third character as 3
print(string1[::-1])  # reverse of a string
print(string1[::-2])  # reverse of a string , every other character as 2
print("Hello"[0])  # allowed
# print("Hello"[10]) # error - index out of range

my_string = input("input is : ")  # input given is string
print(type(my_string))  # Output: <class 'str'>

num_char = len(my_string)  # length of a string
print(type(num_char))  # Output: <class 'int'> - type check , length is int
print("length ",num_char ) # way to concat string with numbers , you cant use '+'. It gives type error

# Type Casting
string_is = str(num_char)  # Converting to str
print(type(string_is))  # Output: <class 'str'> - type check : This error commonly arises when you attempt to use a variable with the same name as a built-in function or method, thus overwriting the built-in functionality

num_as_string = "123"
print(int(num_as_string))  # Output: <class 'int'> - type check
print(float(num_char))  # Output: <class 'float'> - type check 6.0
print(bool(num_char))  # Output: <class 'bool'> - type check true
bool_as_string = "true"
print(bool(bool_as_string))  # Output: <class 'bool'> - type check true
bool_as_string = "false"
print(bool(bool_as_string))  # Output: <class 'bool'> - type check true
num_as_string = "0"
num1 = 0
num2 = 1
print(bool(num_as_string)) # Output: <class 'bool'> - type check true
print(bool(num1))  # Output: <class 'bool'> - type check false **
print(bool(num2))  # Output: <class 'bool'> - type check true

# ** NOTE: Empty String and 0 in int gives boolean false
# int + float = float
print(type(12.5/2)) # float, division o/p is always float
print(2/0.5) # float

# NOTE: If divided by zero : ZeroDivisionError: division by zero

# A variable can also be None
x = None
print(x) # None
print(type(x)) # <class 'NoneType'>


# Below are all false :
print(bool(None))
print(bool(0))
print(bool(""))

x = 123
print(type(str(x))) # Type conversion to string

x: int  # Leave it as is, and later on can give this a value
x = 12
print(x)


def police_check(age: int) -> bool:  # parameter type and return type.
    return True


print(police_check(12))
