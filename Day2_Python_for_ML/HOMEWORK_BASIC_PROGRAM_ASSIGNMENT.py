# #Swapping two numbers
# a, b = map(int, input().split())
# a, b = b, a# Print swapped values
# print(a, b)

# # Area of Cicle
# pi = 3.14
# radius = float(input("Enter the radius of the circle:"))
# area = pi * radius * radius
# print("Area of the circle is:", area)

# #Celsius to Fahrenheit
# Celsius = float(input("Enter temperature in Celsius:"))
# Fahrenheit = (Celsius * 9/5) + 32
# print("Temperature in Fahrenheit:", Fahrenheit)

# #Simple interest
# p, r, t = map(float, input("Enter principal, rate of interest and time:").split())
# SI = (p * r * t) / 100
# print("simple interest is:", SI)

# #Even or Odd
# num = int(input("Enter a number:"))
# if num % 2 == 0:
#     print(num, "is even")
# else:
#     print(num, "is odd")

# #Positive / Negative / Zero
# num = float(input("Enter a number:"))
# if num > 0:
#     print(num, "is positive")

# elif num < 0:
#     print(num, "is negative")

# else:
#     print("The number is zero")


# a, b, c = map(float, input("Enter three numbers:").split())
# if(a > b) and (a > c):
#     print(a, "is the Largest number")

# elif(b > a) and (b > c):
#     print(b, "is the Largest number")

# else:
#     print(c, "is the Largest number")    


# #Leap Year
# Year = int(input("Enter a year:"))
# if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
#     print(Year, "is a Leap Year")

# #Grade from Marks
# marks = int(input("Enter your marks:"))

# if(marks >= 90 and marks <= 100):
#     print("Grade A")
# elif(marks >= 80 and marks < 90):
#     print("Grade B")
# elif(marks >= 70 and marks < 80):
#     print("Grade c")
# elif(marks >= 60 and marks < 70):
#     print("Grade D")
# elif(marks >= 50 and marks < 60):
#     print("Grade E")
# else:
#     print("Grade F")  

# #Multiplication Table
# multiplacation_table = int(input("Enter a number to print its multiplication table:"))
# for i in range(1, 11):
#     print(multiplacation_table, "x", i, "=", multiplacation_table * i)      

# #Sum of first n natural numbers
# n = int(input("Enter a number:"))
# sum = 0
# for i in range(1, n + 1):
#     sum += i
# print("Sum of first", n, "natural numbers is:", sum) 

# #Factorial of a number
# num = int(input("Enter a number to find its factorial:"))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print("Factorial of", num, "is:", factorial)

# #Fibonacci Series
# n = int(input("Enter the number of terms in Fibonacci series:"))
# a, b = 0, 1
# print("Fibonacci Series:")
# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b

# n = int(input("Enter a number of terms in Fibonacci series:"))
# a = 0
# b = 1
# out = []

# for _ in range(n):
#     out.append(str(a))
#     a, b = b, a + b

# print(" ".join(out))    

# #Prime Number Check
# prime_check = int(input("Enter a number to check if it is prime:"))
# is_prime = True
# if prime_check <= 1:
#     is_prime = False
# else:
#     for i in range(2, int(prime_check**0.5) + 1):
#         if prime_check % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print(prime_check, "is a prime number")
# else:
#     print(prime_check, "is not a prime number")

# #Count Digits
# num = input("Enter a number to count its digits:").strip()
# if num.startswith('-'):
#     num = num[1:]

# print("Number of digits in the number is:", len(num))

# #Sum of Digits
# num = int(input("Enter a number to find the sum of its digits:"))
# sum = 0
# while num > 0:
#     digit = num % 10
#     sum += digit
#     num = num // 10

# print("Sum of digits is:", sum)    

# # Reverse a String
# string_reverse = input("Enter a string to reverse it:")
# reversed_string = string_reverse[::-1]
# print("Reversed string is:", reversed_string)

# #Palindrome Check
# palindrome_check = input("Enter a string to check if it is a palindrome:")
# reversed_string = palindrome_check[::-1]
# if palindrome_check == reversed_string:
#     print(palindrome_check, "is a palindrome")  
# else:
#     print(palindrome_check, "is not a palindrome")

# #Count vowels
# string_vowels = input("Enter a string to count the number of vowels:")
# vowel_count = 0
# vowels = "aeiouAEIOU"
# for char in string_vowels:
#     if char in vowels:
#         vowel_count += 1
# print("Number of vowels in the string is:", vowel_count)

# #Count words
# string_words = input("Enter a string to count the number of words:")
# words = string_words.split()
# print("Number of words in the string is:", len(words))

# # Replace Characters
# string_replace = input("Enter a string:")
# char_to_replace = input("Enter the character to be replaced:")
# replacement_char = input("Enter the replacement character:")    
# new_string = string_replace.replace(char_to_replace, replacement_char)
# print("Modified string is:", new_string)

# #Sum of list elements
# num_list = list(map(int, input("Enter list elements separated by space:").split()))
# sum_list = 0
# for num in num_list:
#     sum += num
# print("Sum of list elements is:", sum)

# #Min and Max in a list
# num_list = list(map(int, input("Enter list elements separated by space:").split()))
# min_num = min(num_list)
# max_num = max(num_list)
# print("Minimum number in the list is:", min_num)
# print("Maximum number in the list is:", max_num)

# #Samllest and Largest in a list without using min() and max()
# num_list = list(map(int, input("Enter list elements separated by space:").split()))
# smallest = num_list[0]
# Largest = num_list[0]
# for num in num_list:
#     if num < smallest:
#         smallest = num
#     if num > Largest:
#         Largest = num
# print("Smallest number in the list is:", smallest)
# print("Largest number in the list is:", Largest)    

##Count Occurrences of an element in a list
# num_list = list(map(int, input("Enter list elements separated by space:").split()))
# element = int(input("Enter the element to count its occurrences:"))
# count = 0
# for num in num_list:
#     if num == element:
#         count += 1
# print("Number of occurrences of", element, "in the list is:", count)

 #Even Numbers from a List
# num_list = list(map(int, input("Enter list elements separated by space:").split()))
# even_numbers = []
# for num in num_list:
#     if num % 2 == 0:
#         even_numbers.append(num)
# print("Even numbers in the list are:", even_numbers)

 #Reverse a List (without reverse())\
num_list = list(map(int, input("Enter list elements separated by space:").split()))
reversed_list = []
for i in range(len(num_list) - 1, -1, -1):
    reversed_list.append(num_list[i])   
print("Reversed list is:", reversed_list)