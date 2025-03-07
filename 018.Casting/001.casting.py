# Casting means -- Changing one type of data into another 

# numeric -- int , float 
# string 
# boolean 
# list 
# dictionary 
# tuple etc.

# print("Hello "+ str(123))


# Not every data type can be conveted to another data type.

# print(int("123")+123)
# print(int("Hello113"+100))


# Boolean 
 # true == 1
 # false == 0


#100 , 1 , -11 , "Hello" == True
# 0 ,False ,""
# if "":                            
#     print("This is True")         
# else:
#     print("This is false")


print(True + 100)       # 1+100 = 101

# Implicit casting -- Boolean 

# print(bool(-100)+ 100)     # 1 + 100 = 101

# print(bool(-1)+1)          # 1+1 = 2 

# print(bool(100)+1)           # 1+ 1 = 2

# print(False + 100)           # 0 + 100 = 100


# Float to int <--> int to float

print(int(100.567))

# 3.14 
print(100 + 100.5)

# Float to int --- When you don't require the decimal part of the number (truncate the decimal)

# 130.245

#  130


# int to float ---> When we need more precise results

# print(float(130))

# print(100 + 0.0)
# print(int(130.245))
# print(float(100))

# int to float  -- this is recommended way to casting --- no data loss 

# print(100 + 100.5)

print(3*1.5 +1.5)             # 3*1.5 + 1.5 = 4.5 + 1.5 = 6.0
print(3*1.5 + int(1.5))        # 3*1.5 + 1 = 4.5 +1 = 5.5