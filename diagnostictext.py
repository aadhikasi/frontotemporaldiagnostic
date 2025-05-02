# Importing the necessary files required towards building the system.

import time

# MNE module is important towards the usage of reports to provide clear and accurate data to the people using the system.
import mne


# First function that sets up the landing page of the system.
def symptom_alt():
    print(
        "Diagnostic for FTD (fronto-temporal dementia). Please answer with 'yes' or 'no', then view your score after!")

    while True:
        consent = input("Would you like to proceed? ").strip().lower()
        if consent in ["yes", "no"]:
            break
        print("Invalid, please try again.")

    if consent == "yes":
        # Calls for questions array to be activated.
        question_ftd()
    elif consent == "no":
        print("Thank you. Exiting the program.")
        exit()


# Second function that holds a list of questions and leverages such questions in a "Yes" and "No" format to get responses from users.
def question_ftd():
    score = 0

    # List of questions (Used in an array)
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

    # For loop that selects each question from the array and displays it onto the web server.
    for question in questions:
        while True:
            response = input(question + " ").strip().lower()
            if response in ["yes", "no"]:
                break
            print("Invalid. Try again.")

        # Score changes based on score increasing. This score value is just showing how many out of all the symptoms available that you have.
        if response == "yes":
            score += 1

    print(f"Your score is: {score}")
    follow_up(score)


# Function that prints the score at the end with a gist of what the score means in terms of the diagnosis.
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

    # Loop that calls for an option for the user to get an analysis of the score.
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

    # Phrase that is formed when the score is calculated and produced.

    if score == 0:
        myhtml = f"""
        <p>Here's the score that you received: {score} </p>
        <p>Score description: </p>
        <list>
        <p> 1. You have a high chance of developing...</p>
        <p> 2. You need to improve how your life works. </p>
        <p> 3. You need to promote key healthy habits. </p>
        <p> 4. You need to enforce greater systems in your life. </p>
        </list>
        """
    elif score == 1:
        myhtml = f"""
                <p>Here's the score that you received: {score} </p>
                <p>Score description: </p>
                <list>
                <p> 1. You have a high chance of developing...</p>
                <p> 2. You need to improve how your life works. </p>
                <p> 3. You need to promote key healthy habits. </p>
                <p> 4. You need to enforce greater systems in your life. </p>
                </list>
                """

    elif score == 2:
        myhtml = f"""
                <p>Here's the score that you received: {score} </p>
                <p>Score description: </p>
                <list>
                <p> 1. You have a high chance of developing...</p>
                <p> 2. You need to improve how your life works. </p>
                <p> 3. You need to promote key healthy habits. </p>
                <p> 4. You need to enforce greater systems in your life. </p>
                </list>
                """

    elif score == 3:
        myhtml = f"""
                        <p>Here's the score that you received: {score} </p>
                        <p>Score description: </p>
                        <list>
                        <p> 1. You have a high chance of developing...</p>
                        <p> 2. You need to improve how your life works. </p>
                        <p> 3. You need to promote key healthy habits. </p>
                        <p> 4. You need to enforce greater systems in your life. </p>
                        </list>
                        """

    elif score == 4:
        myhtml = f"""
                        <p>Here's the score that you received: {score} </p>
                        <p>Score description: </p>
                        <list>
                        <p> 1. You have a high chance of developing...</p>
                        <p> 2. You need to improve how your life works. </p>
                        <p> 3. You need to promote key healthy habits. </p>
                        <p> 4. You need to enforce greater systems in your life. </p>
                        </list>
                        """

    elif score == 5:
        myhtml = f"""
                        <p>Here's the score that you received: {score} </p>
                        <p>Score description: </p>
                        <list>
                        <p> 1. You have a high chance of developing...</p>
                        <p> 2. You need to improve how your life works. </p>
                        <p> 3. You need to promote key healthy habits. </p>
                        <p> 4. You need to enforce greater systems in your life. </p>
                        </list>
                        """

    elif score == 6:
        myhtml = f"""
                        <p>Here's the score that you received: {score} </p>
                        <p>Score description: </p>
                        <list>
                        <p> 1. You have a high chance of developing...</p>
                        <p> 2. You need to improve how your life works. </p>
                        <p> 3. You need to promote key healthy habits. </p>
                        <p> 4. You need to enforce greater systems in your life. </p>
                        </list>
                        """

    elif score ==7:
        myhtml = f"""
                        <p>Here's the score that you received: {score} </p>
                        <p>Score description: </p>
                        <list>
                        <p> 1. You have a high chance of developing...</p>
                        <p> 2. You need to improve how your life works. </p>
                        <p> 3. You need to promote key healthy habits. </p>
                        <p> 4. You need to enforce greater systems in your life. </p>
                        </list>
                        """

    elif score ==8:
        myhtml = f"""
                        <p>Here's the score that you received: {score} </p>
                        <p>Score description: </p>
                        <list>
                        <p> 1. You have a high chance of developing...</p>
                        <p> 2. You need to improve how your life works. </p>
                        <p> 3. You need to promote key healthy habits. </p>
                        <p> 4. You need to enforce greater systems in your life. </p>
                        </list>
                        """

    elif score == 9:
        myhtml = f"""
                        <p>Here's the score that you received: {score} </p>
                        <p>Score description: </p>
                        <list>
                        <p> 1. You have a high chance of developing...</p>
                        <p> 2. You need to improve how your life works. </p>
                        <p> 3. You need to promote key healthy habits. </p>
                        <p> 4. You need to enforce greater systems in your life. </p>
                        </list>
                        """

    else:
        myhtml = f"""
                        <p>Here's the score that you received: {score} </p>
                        <p>Score description: </p>
                        <list>
                        <p> 1. You have a high chance of developing...</p>
                        <p> 2. You need to improve how your life works. </p>
                        <p> 3. You need to promote key healthy habits. </p>
                        <p> 4. You need to enforce greater systems in your life. </p>
                        </list>
                        """


    # Create a report using the MNE-Python module. This report intends to show the details of the diagnosis as well as tips to help people feel better.
    report = mne.Report(title="Diagnosis Score Analysis")
    report.add_html(title="Details", html=myhtml)
    report.save("report_raw.html", overwrite=True)


import matplotlib.pyplot as plt

# Auto-generate a new Python script that plots brain deterioration data
plot_script = f'''
import matplotlib.pyplot as plt

# Simulated brain volume data over time (years)
years = list(range(0, 11))
healthy = [100 - y*1.2 for y in years]  # Healthy aging
ftd = [100 - y*3.0 for y in years]      # FTD progression

plt.figure(figsize=(8, 5))
plt.plot(years, healthy, label='Healthy Brain', linestyle='--', marker='o')
plt.plot(years, ftd, label='FTD Brain', linestyle='-', marker='s')

# Mark user's score
plt.axhline(y=100 - {score} * 3, color='red', linestyle=':', label='Your Risk Indicator')

plt.title('Brain Volume Decline Over Time')
plt.xlabel('Years Since Baseline')
plt.ylabel('Brain Volume (% of initial)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the graph
plt.savefig('brain_deterioration.png')
plt.show()
'''

# Write the Python code to a file
with open("plot_output.py", "w") as f:
    f.write(plot_script)

print("\n✅ A new file 'plot_output.py' has been created. Run it to view your brain deterioration graph.")


