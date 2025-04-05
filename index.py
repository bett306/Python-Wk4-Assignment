filename = input("Enter the file name:")

try:
    file = open(filename,'r')
    data = file.read()
    file.close()
except FileNotFoundError:
    print("Error: File does not exist.")
except IOError:
    print("Error: The file can't be read.")
else:
    new_file = open("modified_" + filename,'w')
    new_file.write(data.upper())
    new_file.close()
    print("Modified file saved as 'modified_" + filename + "'")
finally:
    print("Have a nice day😁.")