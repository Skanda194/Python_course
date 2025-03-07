def quiz_game():
    score = 0
    questions = [
        ("How many times can you subtract 5 from 25?", ["Five", "Once", "Six", "Sorry, I can't do that. My Maths is weak."], 2),
        ("Imagine you are in a sinking rowboat surrounded by sharks. How would you survive?", ["I would kill the shark.", "Try to stay in the boat.", "I would stop imagining.", "The shark will decide what to do with me."], 3),
        ("If you are in a dark room with a candle, a wood stove, and a gas lamp, what would you light first?", ["A candle", "A match", "A gas Lamp", "Have a bulb in your room, buddy"], 2),
        ("Bay of Bengal is in which state?", ["West Bengal", "Andhra Pradesh", "Haryana", "Liquid state"], 4),
        ("Which is heavier: 100 pounds of steel or 100 pounds of feathers?", ["Feathers", "Steel", "Both are the same weight", "I need a balance"], 3),
        ("How many things are in a baker's dozen?", ["5", "9", "12", "13"], 4),
        ("Is it legal for a person living in Texas to be buried in Pennsylvania?", ["Yes", "No, it is illegal to bury someone alive"], 2),
        ("How much dirt is in a hole that is 18 feet deep and 4 feet wide?", ["100 pounds", "72 pounds", "14 pounds", "None"], 4)
    ]
    
    print("\n////////////////////////////////////////// WANNA PLAY A FUN QUIZ ////////////////////////////\n")
    
    for i, (question, options, correct) in enumerate(questions, 1):
        print(f"Q{i}. {question}")
        for j, option in enumerate(options, 1):
            print(f"{j}) {option}")
        
        try:
            ans = int(input("Enter your choice: "))
            if ans == correct:
                score += 4
                print(f"Correct! Your total score is: {score}\n")
            else:
                score = max(0, score - 1)
                print(f"Wrong answer. Your total score is: {score}\n")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.\n")
    
    print("------------------------------------------------------------------------------")
    print(f"Quiz Over! Your final score is: {score}")
    print("Thank you for playing!")

if __name__ == "__main__":
    quiz_game()
