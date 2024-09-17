# Finding a word in a file using Python

# This this 
def search_string(filename, word):
    try:
        with open(filename,'r') as f:
            content = f.read()
            frequency = content.lower().count(word.lower())
            print(f"Frequency of {word} is : {frequency}")
    except FileNotFoundError:
        print("File not found.")

search_string('example.txt',"Python")
        