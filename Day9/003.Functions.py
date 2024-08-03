# Passing a value to function

def Display_info(name):
    print(" Hello ," , name)

# Display_info("Arvinder")
# Display_info("Skanda")
# Return Values - Functions can return values also
# Adding two numbers
#v Return keyword

def addition(first, second):
    print(first+ second)

# addition(12,20)

def add(first, second):
    return first + second

sum = add(100, 200)
print(sum)
print(add(100,300))
