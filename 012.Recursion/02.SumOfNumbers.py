def sumOfNumbers(n):
    if n == 0:
        return 
    elif n==1:
        return 1
    else:
        return n + sumOfNumbers(n-1)

result = sumOfNumbers(5)
print(result)