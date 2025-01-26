# Try - Except :

# Error handling module - 

# try:
#     print(y)
# except:
#     print("An exception occured")
# print(5/0)
# try:
#     print(5/0)
# except:
#     print("Can't divide with zero")

# try:
#     print(5//3)
# except:
#     print("Can't divide with zero")
# else:
#     print("I can see that try got executed")


try:
    print(5//3)
except:
    print("Can't divide with zero")
else:
    print("I can see that try got executed")
finally:
    print("I don't care whether try is successful or not.")


try:
    # it is the block where we write our actual logic.
    print(5/0)
except:
    # This will show user an error message if try block fails 
    print("Can't divide with zero")
else:
    # This will print when try got success
    print("I can see that try got executed")
finally:
    # This does not depend on the try block it will execute regardless of what is that status of try block
    print("I don't care whether try is successful or not.")