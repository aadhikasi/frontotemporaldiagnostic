import time


def symptom_alt():
    print("Diagnostic for FTD (fronto-temporal dementia). Please answer with 'yes' or 'no', then view your score after!")

    while True:
        consent = input("Would you like to proceed? ").strip().lower()
        if consent in ["yes", "no"]:
            break
        print("Invalid, please try again.")
    
    if consent == "yes":
        question_ftd()
    elif consent == "no":
        print("Thank you. Exiting the program.")
        exit()


def question_ftd():
    score = 0

    questions = [
        "Do you frequently forget recent events or conversations?",
        "Do you often feel confused about dates, time, or other semantics?",
        "Do you struggle to find the right words during conversations?",
        "Do you find it hard to concentrate or complete familiar tasks?",
        "Have you noticed poor judgment in handling your tasks?",
        "Do you experience sudden mood swings?",
        "Do you have difficulty recognizing familiar faces or places?",
        "Do you frequently make mistakes while performing tasks that you used to do well?",
        "Have you noticed that your speech has become slower or that you stutter more frequently?"
    ]

    for question in questions:
        while True:
            response = input(question + " ").strip().lower()
            if response in ["yes", "no"]:
                break
            print("Invalid. Try again.")
        
        if response == "yes":
            score += 1

    print(f"Your score is: {score}")
    follow_up(score)


def follow_up(score):
    print("\nHere is your analysis!")
    if score == 0:
        print("You show no symptoms of FTD.")
    elif 1 <= score <= 3:
        print("You have mild symptoms. Consider monitoring your condition.")
    elif 4 <= score <= 6:
        print("You have moderate symptoms. Consider consulting a healthcare professional.")
    else:
        print("You have significant symptoms. It's recommended that you seek medical advice immediately.")

    while True:
        follow_up_for_analysis = input("\nWant an analysis of your score? Answer 'yes' or 'no': ").strip().lower()
        if follow_up_for_analysis in ["yes", "no"]:
            break
        print("Invalid input. Please provide an answer per the prompt.")

    if follow_up_for_analysis == "yes":
        print("Thank you for using this tool.")
    elif follow_up_for_analysis == "no":
        print("End of program. Take care!")
        exit()





symptom_alt()
