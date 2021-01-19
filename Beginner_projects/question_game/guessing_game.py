import random

def que():
    questions = ["germany capital?","indian capital?","who is pm of india?"]
    still_guessing = True
    score = 0
    attempt = 0
    correctans = ""
    question = (random.choice(questions))
    if question == questions[0]:
        correctans = "Berlin"
    elif question == questions[1]:
        correctans = "Delhi"
    elif question==questions[2]:
        correctans = "modi"
    print(question)
    guessans= input("please enter your answer::")
    while still_guessing and attempt < 3:
        if guessans.lower() == correctans.lower():
            print("correct answer")
            score += 1
            still_guessing = False
        else:
            if attempt < 2:
                guessans = input("answer is wrong, try again: ")
            attempt += 1
        if attempt==3:
            print("the correct answer is " + correctans )
    print( f"your scoore is ' ' {score} ")

que()