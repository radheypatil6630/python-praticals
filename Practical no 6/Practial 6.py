import os

file = open('demo.txt', 'w')
for each in file:
    print(each)

# Reading only 100 Bytes
with open('sample1.txt', 'r') as file:
    content = file.read(100)
    print("\nRead first 100 bytes:")
    print(content)

# Append
with open('demo.txt', 'a') as file:
    file.write('This is a new line added at the end of the file.\n')
with open('demo.txt', 'r') as file:
    content = file.read()
print("Data appended to sample1.txt\n")
print(content)

# Readline
with open('demo.txt', 'r') as file:
    line = file.readline()
    print("\nRead a single line:")
    print(line)

# Readlines
with open('demo.txt', 'r') as file:
    line = file.readlines()
    print("\nRead a single line:")
    print(line)

# Seek function
with open('demo.txt', 'r') as file:
    file.seek(10)
    content = file.read()
    print("\n", content)

# tell function (gives current cursor position)
with open('demo.txt', 'r') as file:
    print("File Current Cursor is at: ", file.tell())
    content = file.read(100)
    print("\n", content)
    print("File Current Cursor is at: ", file.tell())

# Creating New File
with open('Sample.txt', 'w') as file:
    file.write('This is a new file.')
with open('Sample.txt', 'r') as file:
    content = file.read()
    print("\n", content)

# Create and Delete the Fie
with open('sample3.txt', 'w') as file:
    file.write('This is a new file.')
os.remove('sample3.txt')
print("File 'sample3.txt' deleted.")

# Working Directory
print("Working Direcotry:", os.getcwd())
print("\n")

# Making New Directory
os.mkdir('D:\Py_Lab7')
os.mkdir('D:\Py1_Lab7')
os.rename('D:\\Py1_Lab7', 'F:\\Py2_Lab7')

print("Current directory :", os.getcwd())
# Changing directory
os.chdir('D:\APL')
print("Current directory :", os.getcwd())
