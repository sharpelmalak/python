# python

![Data types in python](1.jpg)

# String Data Types in Python


![string type in python](2.jpg)

## _Creating a String_

In Python, a string is created by enclosing characters within quotes, either single quotes ('...') or double quotes ("...").

```python
string1 = 'Hello, World!'
print(string1)
```

 The code creates a string variable with the value "Hello, World!".


## _Concatenation_

The concatenation of two strings can be performed using the "+" operator.

```python
str1 = "Hello"
str2 = "World"
str3 = str1 + str2
print(str3)
```

In this code, two string variables are created with the values "Hello" and "World". The third variable is created by concatenating the two strings.


## _Repetition_

The repetition of a string can be performed by multiplying it by an integer.


```python
str1 = "Hello"
str2 = str1 * 3
print(str2)
```

This code creates a string variable with the value "Hello" and then multiplies the string to create a new string variable with the value "HelloHelloHello".


## Indexing

In Python, strings are sequences of characters and can be accessed using square brackets "[]" to index individual characters or slices of the string.

Python uses 0-based indexing, which means that the first character in a string has an index of 0, the second character has an index of 1, and so on.

> It's important to note that Python uses 0-based indexing for many data types, including lists, tuples, and arrays.

```python
str1 = "Hello World"
print(str1[0])
```

In the code, we create a string variable str1 with the "Hello World" value. We then retrieve the first character from the string by accessing its index.

## Slicing

In Python, you can use slicing to extract a specific portion of a string by specifying the starting and ending indices.

To slice a string, use the syntax string[start_index:stop_index], where start_index is the index of the first character to include in the slice, and stop_index is the index of the first character to exclude from the slice.


> It's important to keep in mind that the stop index is not included in the slice.

> If the start index is omitted, Python assumes that it should start from the beginning of the string. Similarly, if the stop index is omitted, Python assumes it should slice until the end of the string.


```python
str1 = "Hello World"
print(str1[0:5])
```

In the given code, a string variable str1 with the value "Hello World" is created, and a portion of the string is retrieved using slicing.

## Length

You can find the length of a string by using the len() function. The length of a string is represented by the number of characters.

```python
str1 = "Hello World"
print(len(str1))
```

The code creates a string variable with the value "Hello World" and then finds the length of the string.


## Finding Substrings

The "in" operator checks if a substring is present in a string.


```python
str1 = "Hello World"
print("World" in str1)
```

This code creates a string variable "Hello World" and then checks if the substring "World" is present in the string.


## Replacing Substrings

The replace() method can be used to replace a substring in a string.


```python
str1 = "Hello World"
str2 = str1.replace("World", "Universe")
print(str2)
```

This code creates a string variable with the value "Hello World" and then replaces the substring "World" with the substring "Universe" and return new string without update str1.

## Converting to Uppercase/Lowercase

The upper() and lower() methods can be used to convert a string to uppercase or lowercase, respectively.

```python
str1 = "Hello World"
print(str1.upper())  
print(str1.lower())
```

This code creates a string variable with the value "Hello World" and then converts the string to uppercase and lowercase.


## Stripping Whitespaces

The strip() method can be used to remove whitespaces from the beginning and end of a string.

```python
str1 = " Hello World "
print(str1.strip())
```

the above code creates a string variable with whitespaces at the beginning and end and then removes the whitespaces from the string.

## Splitting into List

In Python, the split() method can be utilized to break down a string into a list of smaller substrings based on a specified delimiter.




> It's important to remember that the split() method can use any specified delimiter to divide the string into smaller substrings, including commas, semicolons, or other characters.

> In the absence of a specified delimiter, the method will utilize whitespace as the default delimiter to split the string.

```python
str1 = "Hello World"
str_list = str1.split(" ")
print(str_list)
```

The provided code initializes a string variable called str1 with the value "Hello World" and then splits the string into a list of substrings using the delimiter " ".

## F-String Literals

Python has another type of string literal called formatted strings or f-strings for short. F-strings allow you to interpolate values into your strings and format them as you need.

To build f-string literals, you must prepend an f or F letter to the string literal. Because the idea behind f-strings is to interpolate values and format them into the final string, you need to use something called a replacement field in your string literal. You create these fields using curly brackets.

```python
name = "Jane"
print(f"Hello, {name}!")
```

## String common methods

| Method	                 | Description |
| ------	                 | ----------- |
|.capitalize()	             | Converts the first character to uppercase and the rest to lowercase |
|.casefold()	             | Converts the string into lowercase |
|.center(width[, fillchar])	 | Centers the string between width using fillchar |
|.expandtabs(tabsize)	     | Replaces tab characters with spaces according to tabsize |
|.format(*args, **kwargs)	 | Interpolates and formats the specified values |
|.format_map(mapping)	     | Interpolates and formats the specified values using a dictionary |
|.join(iterable)	         | Joins the items in an iterable with the string as a separator |
|.ljust(width[, fillchar])	 | Returns a left-justified version of the string |
|.rjust(width[, fillchar])	 | Returns a right-justified version of the string |
|.lower()	                 | Converts the string into lowercase |
|.strip([chars])	         | Trims the string by removing chars from the beginning and end |
|.lstrip([chars])	         | Trims the string by removing chars from the beginning |
|.rstrip([chars])	         | Trims the string by removing chars from the end |
|.removeprefix(prefix, /)	 | Removes prefix from the beginning of the string |
|.removesuffix(suffix, /)	 | Removes suffix from the end of the string |
|.replace(old, new [, count])|	Returns a string where the old substring is replaced with new |
|.swapcase()	             |Converts lowercase letters to uppercase letters and vice versa|
|.title()	|Converts the first character of each word to uppercase and the rest to lowercase|
|.upper()	|Converts a string into uppercase|
|.zfill(width)	|Fills the string with a specified number of zeroes at the beginning|



<br>

> ### All string methods return new values. They do not change the original string.

<br>
<br>
<br>

# Numeric Data Types in Python

![Numeric Data Types in Python](3.jpg)

<br>

In Python, integers, floating-point numbers, and complex numbers are used to represent different types of numbers.

## Integer Numbers

Integer numbers are whole numbers with no decimal places. They can be positive or negative numbers. For example, 0, 1, 2, 3, -1, -2, and -3 are all integers.

```python
type(42)
```
## Integer Literals

When you need to use integer numbers in your code, you’ll often use integer literals directly. Literals are constant values of built-in types spelled out literally, such as integers.

> Python provides a few different ways to create integer literals. The most common way is to use base-ten literals that look the same as integers look in math

> Python has no limit to how long an integer value can be. The only constraint is the amount of memory your system has. Beyond that, an integer can be as long as you need.

> For a really, really long integer, you can get a ValueError when converting it to a string
```python
>>> 123 ** 10000
Traceback (most recent call last):
  ...
ValueError: Exceeds the limit (4300 digits) for integer string conversion;
            use sys.set_int_max_str_digits() to increase the limit
```

If you need to print an integer number beyond the 4300-digit limit, then you can use the sys.set_int_max_str_digits() function to increase the limit and make your code work.

> When you’re working with long integers, you can use the underscore character to make the literals more readable

> Do you know how to represent Binary, Octal , HexaDecimal in python ?

> yes using prefix 0b or 0B for Binary, 0o or 0O for octal, 0x or 0X for hexa

## Floating-point numbers

Floating-point numbers, or just float, are numbers with a decimal place. For example, 1.0 and 3.14 are floating-point numbers. You can also have negative float numbers, such as -2.75. In Python, the name of the float class represents floating-point numbers.

## Complex Number Literals

In Python, you can define complex numbers using literals that look like a + bj, where a is the real part, and bj is the imaginary part.

```python 
print(2 + 3j)
print(7j)
print(2.4 + 7.5j)
print(3j + 5)
print(5 - 3j)
print(1 + j)
```


## Basic Arithmetic Operations

```python
a = 5
b = 3

# Addition
c = a + b
print(c) 

# Subtraction
c = a - b
print(c) 

# Multiplication
c = a * b
print(c) 

# Division
c = a / b
print(c)

# Modulo

a = 7
b = 3

c = a % b
print(c)

# Integer Division

c = a // b
print(c) 

# Exponentiation

a = 2
b = 3

c = a ** b
print(c) 

```

## Type Conversion

Type conversion allows for converting a number from one data type to another, such as from integer to float or vice versa.


The float() function converts a number to a floating-point value, while the int() function converts a number to an integer value.

```python

a = 5
c_num = 3 + 4j

d = float(a)

c_real_float = float(c_num.real)
c_real_int = int(c_num.real)
c_imag_float = float(c_num.imag)
c_imag_int = int(c_num.imag)

print("Float value of a:", d)
print("Float value of the real component of c_num:", c_real_float)
print("Integer value of the real component of c_num:", c_real_int)
print("Float value of the imaginary component of c_num:", c_imag_float)
print("Integer value of the imaginary component of c_num:", c_imag_int)
```
# Boolean Data Type

This data type holds truth values and lays the base for logical operations and conditional statements. It has only two possible values: It contains questions and answers in True and False. These are very useful in deciding whether a program should continue or move to a different location within a program depending on some condition.

```python
is_user_authenticated = True
is_prime_number = False


### Conditional statement (if-else)

if is_user_authenticated:
    print("Welcome back!")
else:
    print("Please log in.")
# Logical operators (and, or, not)
is_admin = is_user_authenticated and has_admin_privileges
```

# Collections in Python

We have gone through the basic elements for describing simple data values. Now, it is time to discuss a wide array of data structures provided by Python to work with more complex data arrangements.


### There are four collection data types in the Python programming language:

1- List is a collection which is ordered and changeable. Allows duplicate members.
<br>
2- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
<br>
3- Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
<br>
4- Dictionary is a collection which is ordered** and changeable. No duplicate members.
<br>

> *Set items are unchangeable, but you can remove and/or add items whenever you like.

> **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

## Lists (list): 

They are ordered collections of items that are enclosed in square brackets [] and are mutable. They can contain any fragments of various data types, making them rather flexible. Elements can be addressed based on the position of the list and you can change array elements, you can append and delete new elements from the list.

```python

shopping_list = ["apples", 2.5, "milk", True]  # Mix of data types

# Accessing elements by index (zero-based)
first_item = shopping_list[0]  # "apples"
quantity_of_milk = shopping_list[2]  # "milk" (remember indexing starts from 0)
is_found = shopping_list[-1]  #Negative indexing means start from the end



# Modifying elements
shopping_list[1] = 3.0  # Change quantity to 3.0

#slicing list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1:-1])

# Adding elements (append to the end)
shopping_list.append("bread")

#inserting in specific index 
shopping_list.insert(2, "watermelon")

#extending from list or any iterable
thislist.extend(shopping_list)
print(thislist)

# Removing elements
shopping_list.remove("milk")  # Removes the first occurrence of "milk"
shoping_list.pop(1) #Removes the specified index.
del shoping_list[0] #Removes the specified index.
del shoping_list    #Removes list completely.
shoping_list.clear() #empties the list.


#sorting
shoping_list.sort() #Sort List Alphanumerically
shoping_list.sort(reverse = True) #To sort descending, use the keyword argument reverse = True

#copy list three ways

new_list = shoping_list.copy()
new_list = list(shoping_list)
new_list = shoping_list[:]

#join two lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2

```
### Key Takeaways:

Lists are mutable, allowing for dynamic changes.

Use indexing for element access (remember 0-based indexing).

Leverage methods like append(), insert(), remove(), and pop() for list manipulation.


![list methods](4.jpg)

## Tuples (tuple)

Tuples defined with parentheses () are ordered like lists but are immutable.

This maintains data consistency and makes tuples most appropriate in cases where data should not change after being entered or inputted.

```python

# Example: Employee record (immutable)
employee_record = ("Alice", 32, "Software Engineer")

# Accessing elements by index
name = employee_record[0]  # "Alice"

# Attempting modification (results in a runtime error)
# employee_record[1] = 33  # Immutable, this line would cause an error
y = list(employee_record)
y[1] = 33
employee_record = tuple(y)
print(employee_record)

# Creating a new tuple with modifications
updated_record = (employee_record[0], employee_record[1] + 1, employee_record[2])

```
### Key Takeaways

Tuples are immutable, offering data integrity.

Use indexing for element access, similar to lists.

To modify data, create a new tuple with the desired changes.

## Sets (set)

Sets are denoted by curly braces {}. It is an orderless and duplicate-less collection of items. Note that when we add elements to a set, duplicate entries are eliminated on their own. It can be used in operations that involve checking for membership, eliminating redundancy in a list, and set operations such as union, intersection, and difference.

```python


 # Example: Unique website visitors in a month
visitors = {"Alice", "Bob", "Charlie", "Alice"}  # Duplicates are ignored

# Checking for membership we cannot access by index 
is_member = "David" in visitors  # False

# Adding elements
visitors.add("David")

# update from another iterable
visitors.update(("waleed","samy"))

# Removing elements
visitors.remove("Bob")  # Removes "Bob" if present else raise error
visitors.discard("Bob")  # Removes "Bob" if present else will not raise error
visitors.pop()  #remove random element
visitors.clear()  #empty set

# Set operations (assume another set named registered_users)
common_visitors = visitors & registered_users  # Intersection (common elements)
all_visitors = visitors | registered_users  # Union (all unique elements)

```

### Key Takeaways

Sets are unordered and contain unique elements.

Use methods like add(), remove(), and in for element manipulation and membership checks.

True and 1 is considered the same value:

### There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.



 

## Dictionaries (dict)

Dictionaries keys and values are enclosed in curly braces {} to distinguish them from lists while values and keys are separated by colons.: 

A key can be for example a string or a number and it cannot be changed or repeated while a value can be of any type.


```python

# creating a dictionary
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "England": "London"
}

# access the value of keys
print(country_capitals["Germany"])    # Output: Berlin
print(country_capitals["England"])    # Output: London

# add an item with "Italy" as key and "Rome" as its value
country_capitals["Italy"] = "Rome"

# delete item having "Germany" key
del country_capitals["Germany"]

# clear the dictionary
country_capitals.clear()

# change the value of "Italy" key to "Rome"
country_capitals["Italy"] = "Milan"


#membership test
file_types = {
    ".txt": "Text File",
    ".pdf": "PDF Document",
    ".jpg": "JPEG Image",
}

# use of in and not in operators it checks on key only 
print(".pdf" in file_types)       # Output: True
print(".mp3" in file_types)       # Output: False
print(".mp3" not in file_types)   # Output: True

```
## Key Takeaways

Dictionaries provide a way to store data into key-value pairs which makes it very useful in data storage.

Keys must be unique and unalterable (for example, of string or numeric type)

Values can be of any data type which means they are not limited to specifying one.

![dict methods](5.jpg)
