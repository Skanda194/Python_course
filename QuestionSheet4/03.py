def star_pattern(rows):
    for i in range (rows):
        for j in range(i+1):
            print("*",end=" ")
        print()
star_pattern(3)