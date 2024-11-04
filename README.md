# PYTHON_FILE_AND_EXCEPTION_HANDLING
This repository demonstrating file handling and exception management techniques for robust file operations.

# Exercise 1: Write a Python program to read a file and display its contents

file1=open("C:\\Users\\SIXCOUSER\\Desktop\\DSML\\Python\\ASSIGNMENTS\\Assignment 5\\sample.txt",'r')

print(file1.read())

![q1](https://github.com/user-attachments/assets/5da9155c-846f-4a29-b882-109c86cfd7e5)

# Exercise 2: Write a Python program to copy the contents of one file to another file

source_filename = input("Please enter the source filename: ")

destination_filename = input("Please enter the destination filename: ")

try:

    source_file =  open(source_filename, 'r')
    
    destination_file = open(destination_filename, 'w')
    
    contents = source_file.read()
    
    destination_file.write(contents)
    
    print("Contents copied successfully!")
    
except FileNotFoundError:

    print(f"Error: The file '{source_filename}' was not found.")
    
except IOError as e:

    print(f"An I/O error occurred: {e}")
    
except Exception as e:

    print(f"An unexpected error occurred: {e}")
    
source_file.close()

destination_file.close()

![q2_source_file](https://github.com/user-attachments/assets/588c654d-bc5d-48f1-ab4d-669d81b22f1b)

![q2_1](https://github.com/user-attachments/assets/7c7378f1-914a-4a35-8d34-7c348c3331e3)

![q2_2](https://github.com/user-attachments/assets/257c4426-fd09-477c-a231-f64ff3387f56)

# Exercise 3: (score : 2) Write a Python program to read the content of a file and count the total number of words in that file.

filename = input("Please enter the filename to read: ")

try:

    file = open(filename, 'r')
    
    content = file.read()
    
    print(content)
    
    words = content.split()
    
    word_count = len(words)

    print(f"The total number of words in the file is: {word_count}")

except FileNotFoundError:

    print(f"Error: The file '{filename}' was not found.")
    
except IOError as e:

    print(f"An I/O error occurred: {e}")
    
except Exception as e:

    print(f"An unexpected error occurred: {e}")

![q3](https://github.com/user-attachments/assets/1268b318-dfb7-451c-9443-901b6bc0d6ae)

# Exercise 4: (score : 1) Write a Python program that prompts the user to input a string and converts it to an integer. Use try-except blocks to handle any exceptions that might occur

user_input = input("Please enter a number: ")

print("Type of string before converting: ",type(user_input))

try:

    converted_to_integer = int(user_input)
    
    print(f"The converted integer is: {converted_to_integer}")
    
    print("Type of string after converting: ",type(converted_to_integer))
    
except ValueError:

    print("Error: The input is not a valid integer.")

![q4_1](https://github.com/user-attachments/assets/9a7c3dc1-01f9-4f86-b9f7-e314000c2e42)

![q4_2](https://github.com/user-attachments/assets/72809a59-ad7d-4e89-842b-58f07437bf7d)

# Exercise 5: (score : 1) Write a Python program that prompts the user to input a list of integers and raises an exception if any of the integers in the list are negative.

user_input = input("Please enter a list of integers separated by spaces: ")

try:

    integer_list = [int(num) for num in user_input.split()]
    
    for num in integer_list:
    
        if num < 0:
        
            raise ValueError(f"Negative integer found: {num}")

    print("All integers are non-negative.")
    
except ValueError as e:

    print(f"Error: {e}")

![q5_1](https://github.com/user-attachments/assets/2fabb34e-341b-4bde-9466-33bca954cbcf)

![q5_2](https://github.com/user-attachments/assets/bb7742f4-7490-4df8-8bd8-1dd963262fda)

# Exercise 6: (score : 2) Write a Python program that prompts the user to input a list of integers and computes the average of those integers. Use try-except blocks to handle any exceptions that might occur.use the finally clause to print a message indicating that the program has finished running.

user_input = input("Please enter a list of integers separated by spaces: ")

try:

    integer_list = [int(num) for num in user_input.split()]
    
    average = sum(integer_list) / len(integer_list)
    
    print(f"The average of the entered integers is: {average}")

except ValueError as e:

    print(f"Error: {e}")
    
except ZeroDivisionError:

    print("Error: Cannot calculate the average of an empty list.")
    
except Exception as e:

    print(f"An unexpected error occurred: {e}")
    
finally:

    print("Program has finished running.")

![q6_1](https://github.com/user-attachments/assets/77e00087-0972-413c-8bce-4f6f430e3c95)

![q6_2](https://github.com/user-attachments/assets/05af0fc7-74ca-4686-b78c-34f2b00f11ba)

![q6_3](https://github.com/user-attachments/assets/f0cc2ebe-0f4a-425d-8835-f6afaae9c12c)

# Exercise 7 : (score : 2) Write a Python program that prompts the user to input a filename and writes a string to that file. Use try-except blocks to handle any exceptions that might occur and print a welcome message if there is no exception occurred.

filename = input("Please enter the filename to write to: ")

content = "Hello, This is a sample string written to the file."

try:

    with open(filename, 'w') as file:
    
        file.write(content)
        
    print("Welcome! The string has been successfully written to the file.")
    
except Exception as e:

    print(f"An error occurred: {e}")

![q7_1](https://github.com/user-attachments/assets/c3e41f57-f1a5-4a1c-9895-c99de0c304f6)

![q7_2](https://github.com/user-attachments/assets/2d04318a-8351-486b-a8c0-642300ae0f92)






