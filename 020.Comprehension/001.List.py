# List Comprehension 

# [expression for item in iterable if condition]

# Write a code to double every number in a range
# doubled =[]
# for x in range(1,5):
#     doubled.append(x*2)

# print(doubled)

# doubledComp=[x*2 for x in range(1,5)]
# print(doubledComp)


# Even Number -- 10 
# 

# even_num = []
# for i in range(1,11):
#     if i%2==0:
#         even_num.append(i)
# print(even_num) 


# even_comp = [x for x in range(1,11) if x%2==0]
# print(even_comp)

# divisible23=[]
# for i in range(1,20):
#     if i%2==0 and i%3==0:
#         divisible23.append(i)
# print(divisible23)


# div_23_comp = [x for x in range(1,20) if x%2==0 if x %3==0]
# print(div_23_comp)

# Dictionary Comprehension:
# {key:value for item in iterable if condition}
# sqr ={}
# for i in range(1,11):
#     sqr[i]= i*i
# print(sqr)


# sqr_comp = {x:x*x for x in range(1,11)}
# print(sqr_comp)


# Hello -- h-1 e -1 l-2 0-1 
text= "hello"
char_count={}
for char in text:
    char_count[char]= text.count(char)

print(char_count)


charCount_comp = {char:text.count(char) for char in text}
print(charCount_comp)



# Set  comprehension 

# [1,3,4,6,7,9] -- 3 === 1 , 0 , 1 , 0 , 1 , 0 

remainders=set()

for i in [1,3,4,6,7,9]:
    remainders.add(i%3)

print(remainders)


remainder_comp = {x%3 for x in [1,3,4,6,7,9]}
print(remainder_comp)