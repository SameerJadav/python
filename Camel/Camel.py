camelCase = input("camelCase: ")
#end="" will start new line at the end of the string, in some ways it can be used as print()
print("snake_case: ", end="")

for letter in camelCase:

    #.isupper() will check for any uppercase letters
    #where-ever there is an uppercase letter print "_" and print everthing in lowercase
    if letter.isupper():
        print("_" + letter.lower() , end="")
    else:
        print(letter , end="")

#if we don't add print(), $ will be add in the end of the line
print()