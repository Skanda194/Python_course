def Fixed_Triangle(rows):
    for i in range(1, rows+1):
        for _ in range(rows-i):
            print(" ", end="")
        for _ in range(i):
            print("*",end="")
        print()
Fixed_Triangle(17)
