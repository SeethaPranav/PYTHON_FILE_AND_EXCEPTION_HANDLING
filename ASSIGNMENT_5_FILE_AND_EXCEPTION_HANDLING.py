# Exercise 1: (score : 1)Write a Python program to read a file and display its contents
#
# file1=open("C:\\Users\\SIXCOUSER\\Desktop\\DSML\\Python\\ASSIGNMENTS\\Assignment 5\\sample.txt",'r')
# print(file1.read())
#
# Exercise 2: (score : 1) Write a Python program to copy the contents of one file to another file
#
# source_filename = input("Please enter the source filename: ")
# destination_filename = input("Please enter the destination filename: ")
#
# try:
#     source_file =  open(source_filename, 'r')
#     destination_file = open(destination_filename, 'w')
#     contents = source_file.read()
#     destination_file.write(contents)
#     print("Contents copied successfully!")
# except FileNotFoundError:
#     print(f"Error: The file '{source_filename}' was not found.")
# except IOError as e:
#     print(f"An I/O error occurred: {e}")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
# source_file.close()
# destination_file.close()
#
# Exercise 3: (score : 2) Write a Python program to read the content of a file and count the total number of words in that file.
#
# filename = input("Please enter the filename to read: ")
# try:
#     # Open the file in read mode
#     file = open(filename, 'r')
#     content = file.read()
#     print(content)
#     words = content.split()
#     word_count = len(words)
#
#     print(f"The total number of words in the file is: {word_count}")
#
# except FileNotFoundError:
#     print(f"Error: The file '{filename}' was not found.")
# except IOError as e:
#     print(f"An I/O error occurred: {e}")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
#
# Exercise 4: (score : 1) Write a Python program that prompts the user to input a string and converts it to an integer.
# Use try-except blocks to handle any exceptions that might occur
#
# user_input = input("Please enter a number: ")
# print("Type of string before converting: ",type(user_input))
# try:
#     converted_to_integer = int(user_input)
#     print(f"The converted integer is: {converted_to_integer}")
#     print("Type of string after converting: ",type(converted_to_integer))
# except ValueError:
#     print("Error: The input is not a valid integer.")
#
#
# Exercise 5: (score : 1) Write a Python program that prompts the user to input a list of integers and
# raises an exception if any of the integers in the list are negative.
#
# user_input = input("Please enter a list of integers separated by spaces: ")
# try:
#     integer_list = [int(num) for num in user_input.split()]
#     for num in integer_list:
#         if num < 0:
#             raise ValueError(f"Negative integer found: {num}")
#
#     print("All integers are non-negative.")
# except ValueError as e:
#     print(f"Error: {e}")
#
#
# Exercise 6: (score : 2) Write a Python program that prompts the user to input a list of integers and computes the average of those integers.
# Use try-except blocks to handle any exceptions that might occur.
# use the finally clause to print a message indicating that the program has finished running.

# user_input = input("Please enter a list of integers separated by spaces: ")
#
# try:
#     integer_list = [int(num) for num in user_input.split()]
#     average = sum(integer_list) / len(integer_list)
#     print(f"The average of the entered integers is: {average}")
#
# except ValueError as e:
#     print(f"Error: {e}")
# except ZeroDivisionError:
#     print("Error: Cannot calculate the average of an empty list.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
# finally:
#     print("Program has finished running.")
#
# Exercise 7 : (score : 2) Write a Python program that prompts the user to input a filename and writes a string to that file.
# Use try-except blocks to handle any exceptions that might occur and print a welcome message if there is no exception occurred.
#
# filename = input("Please enter the filename to write to: ")
# content = "Hello, This is a sample string written to the file."
# try:
#     with open(filename, 'w') as file:
#         file.write(content)
#     print("Welcome! The string has been successfully written to the file.")
# except Exception as e:
#     print(f"An error occurred: {e}")
#
#
#
#
