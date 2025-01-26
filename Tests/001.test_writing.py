
n = int(input("Enter a number: "))
if n%3==0:
    print("Fizz")
elif n%5==0:
    print("Buzz")
elif n%3 and n%5:
    print("FizzBuzz")
else:
    print("Not divisible")

