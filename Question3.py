def checkPallindrome(str):
    if str.lower() == str[::-1].lower():
        return True
    else:
        return False


string = input("Enter a string/word: ")
result = checkPallindrome(string)
if result:
    print(string, " is pallindrome")
else:
    print(string, " is not pallindrome")


