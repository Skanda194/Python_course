# This is the content of my new file.this I am new to Python coding.

# this  - 

# is -    1 
# the -    1
# new - 2
# 

def word_frequency(filename): 
    try:
        with open(filename,'r') as f:
            content = f.read()
            # print(content)
            word_list = content.split()
            word_dictionary={}

            for word in word_list:
                word = word.strip('.,?!:;')
                word = word.lower()

                if word in word_dictionary:
                    word_dictionary[word]+=1
                else:
                    word_dictionary[word]=1
                
            for word , frequency  in word_dictionary.items():
                print(f"{word}:{frequency}")
                
    except FileNotFoundError:
        print("File not found.")

word_frequency('example.txt')


