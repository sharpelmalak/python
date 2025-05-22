# creating strings
# why we may use single or double ?

string1 = 'Hello, World!'
string2 = string1[:]


# string2 = "Hello, World!"
# print(string1)
# print(string2)


#concat

# str1 = "Hello, "
# str2 = "World"
# str3 = str1 + str2
# print(str3)

#repeat

# str1 = "Hello"
# str2 = str1 * 3
# print(str1)
# print(str2)

#index

# str1 = "Hello World"
# print(str1[0])

#slicing

# str1 = "Hello World"
# str2 = str1
# print(str2)

#length

# str1 = "Hello World"
# print(len(str1))


#finding substring

#str1 = "Hello World"
#print( "World" in str1)

#print(str1.find('l')) # not found -1 , or first occuernce of character

#replacing substring

# str1 = "Hello, World! "
# str2 = str1.replace("World", "Universe")
# print(str2)
# print(str1)

#converting to Uppercase/Lowercase

# str1 = "Hello World"
# print(str1.upper())  
# print(str1.lower())
# print(str1)

#stripping whitespaces

# str1 = " Hello World "
# print(len(str1.strip()))
# print(len(str1))

# print(type("Hello"))
# print(type([]))
# print(type(1))
# print(type(1.5))
# print(type(()))
# print(type(None))
# splitting into list

# str1 = "Hello World my name is sharbel"
# str_list = str1.split("m")
# print(str_list)

#f-string

# name = "Ghost"
# let = 8
# print(f"Hello,{name} , {let*name}")


# None

# print(type('hello'))
# print(type(-100000))
# print(type(-100000.0))
# print(type(0B100000))
# print(type(0o100000))
# print(type(0x100000))
# print(type(15+1j))
# print(type(None))

# numbers

#Decimal      base 10
#Binary       base 2
#Octal        base 8
#HexaDecimal  base 16



# cmp = complex(5,2)
# cmp1 = 5 + 2j

# print(cmp)
# print(type(cmp))

# # conversion

# print(int(5.5))
# print(int("5"))
# print(int("0b100000", base=2))
# print(int("10", base=8))
# print(int("10", base=16))


# a = 5
# c_num = 3 + 4j

# d = float(a)

# c_real_float = float(c_num.real)
# c_real_int = int(c_num.real)
# c_imag_float = float(c_num.imag)
# c_imag_int = int(c_num.imag)

# print("Float value of a:", d)
# print("Float value of the real component of c_num:", c_real_float)
# print("Integer value of the real component of c_num:", c_real_int)
# print("Float value of the imaginary component of c_num:", c_imag_float)
# print("Integer value of the imaginary component of c_num:", c_imag_int)





#lists


shopping_list = ["apples", 2.5, "milk", True]  # Mix of data types

# Accessing elements by index (zero-based)
# first_item = shopping_list[0]  # "apples"
# quantity_of_milk = shopping_list[2]  # "milk" (remember indexing starts from 0)
# is_found = shopping_list[-1]  #Negative indexing means start from the end



# # Modifying elements
# shopping_list[1] = 3.0  # Change quantity to 3.0
# shopping_list[2] = False  # Change quantity to 3.0
# print(shopping_list)

# #slicing list

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
len(thislist)
thislist.pop(2)
del thislist[2]
thislist.clear()
del thislist
print(thislist)
# print(thislist[1:2])

# # Adding elements (append to the end)
# shopping_list.append("bread")

# # #inserting in specific index 
# shopping_list.insert(2, "watermelon")

# print(shopping_list)
# #extending

# thislist.extend(shopping_list)
# print(thislist)

# # Removing elements
# shopping_list.remove("milk")  # Removes the first occurrence of "milk"


# # creating a dictionary
# country_capitals = {
#   "Germany": "Berlin", 
#   "Canada": "Ottawa", 
#   "England": "London"
# }

# # access the value of keys
# print(country_capitals["Germany"])    # Output: Berlin
# print(country_capitals["England"])    # Output: London

# # add an item with "Italy" as key and "Rome" as its value
# country_capitals["Italy"] = "Rome"

# # delete item having "Germany" key
# del country_capitals["Germany"]

# # clear the dictionary
# #country_capitals.clear()

# # change the value of "Italy" key to "Rome"
# country_capitals["Italy"] = "Milan"


# #membership test
# file_types = {
#     ".txt": "Text File",
#     ".pdf": "PDF Document",
#     ".jpg": "JPEG Image",
# }

# # use of in and not in operators it checks on key only 
# print(".pdf" in file_types)       # Output: True
# print(".mp3" in file_types)       # Output: False
# print(".mp3" not in file_types)   # Output: True







