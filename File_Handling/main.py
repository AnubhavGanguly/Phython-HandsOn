from fileHelper import FileHelper

file = FileHelper("data.txt", "Hello Anubhav")

# file.create_file()
# file.readFile()
# file.updateFile("Good Morning")
# file.writeFile("Overwriting the file with new content")
# file.deleteFile()













# Create a file
# FileHelper.create_file("data.txt")

# Read a file
# fileContext = FileHelper.readFile("data.txt")
# print(fileContext)

# Append data to my file
# FileHelper.updateFile("data.txt","Updating file content using OOPS concept")

# Overwrite the content of the file
# FileHelper.writeFile("data.txt","Hello Anubhav")

# Delete file
# FileHelper.deleteFile("datas.txt")

# Read the entire file and print it.
# with open ("data.txt",'r') as file:
#     content = file.read()
#     print(content)

#Read the file line by line.
# with open ("data.txt",'r') as file:
#     # Removing newline character(\n) using strip()
#     print(file.readline().strip())
#     print(file.readline())

# Add new text to the file without deleting the old text.
# with open ("data.txt",'a') as file:
#     file.write("\nManipulating data.txt file")
# with open ("data.txt",'r') as file:
#     content= file.read()
#     print(content)


# Overwrite the file with new content.
# with open ("data.txt",'w') as file:
#     file.write("Overwriting the file with new content")

# Try opening a file that doesn't exist and handle FileNotFoundError.
# try:
#     with open ("data.txt",'r') as file:
#         content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("File not found")

# from datetime import datetime

# current_time = datetime.now()

# print(current_time.strftime("%Y-%m-%d"))

