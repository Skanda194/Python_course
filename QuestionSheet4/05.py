def multiplication(number):
    print("Multiplication table{number}")
    for i in range(1,11):
        product= number*i
        print(f"{number}x{i}={product}")
multiplication(5)