# A program to count number of words in a file

def count_words(filename):
    try:
        with open(filename ,'r') as f:
            content = f.read()   #This is the file created to count the words.
            # print("content:",content)
            words = content.split('-')    #splitting on the basis of spaces
            # space , hyphen , comma , semicolon 
            # print("Words:",words)

            words_count = len(words)
            print("Number of words in the input file are :",words_count)
    except FileNotFoundError:
        print("File not found.")


count_words('comma.txt')



