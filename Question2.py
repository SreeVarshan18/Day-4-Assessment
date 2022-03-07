data = input("Enter a string: ")
str_length = len(data)
newfile = open("data.txt", "w")
filedata = newfile.write(str(str_length))
