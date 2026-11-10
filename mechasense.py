# MECHASENSE - MECHATRONICS KNOWLEDGE ASSESSMENT

topics = [
    "PLC and Automation",
    "Sensors and Instrumentation",
    "Microcontrollers",
    "Electrical Circuits",
    "Electrical Machines"
]

questions = [
    "What does PLC stand for?",
    "Which PLC component executes the control program?",
    "Which PLC programming language uses graphical contacts and coils?",

    "Which sensor measures distance using sound waves?",
    "Which sensor detects changes in temperature?",
    "What is the main purpose of a proximity sensor?",

    "What is the main function of a microcontroller?",
    "Which Arduino board is commonly based on ATmega328P?",
    "What does GPIO stand for?",

    "A circuit has a voltage of 12V and current of 2A. Calculate its resistance.",
    "Two resistors of 10 ohms and 20 ohms are connected in series. Find total resistance.",
    "Which component limits current in a circuit?",

    "Which machine converts electrical energy into mechanical energy?",
    "What is the function of a transformer?",
    "Which type of motor operates using electromagnetic induction?"
]

options = [
    ["Programmable Logic Controller", "Power Line Control", "Program Level Computer", "Personal Logic Circuit"],
    ["Power supply", "CPU", "Input module", "Output module"],
    ["Ladder Logic", "HTML", "Python", "CSS"],

    ["Temperature sensor", "Ultrasonic sensor", "Pressure sensor", "Light sensor"],
    ["Thermistor", "Motor", "Relay", "Capacitor"],
    ["Detecting nearby objects", "Generating electricity", "Storing energy", "Increasing voltage"],

    ["Controlling embedded systems", "Storing fuel", "Generating electricity", "Measuring pressure"],
    ["Arduino Uno", "Arduino Mega", "Arduino Due", "Arduino Leonardo"],
    ["General Purpose Input/Output", "General Program Internal Operation", "Global Power Input Output", "General Processing Input Option"],

    ["4 ohms", "6 ohms", "12 ohms", "24 ohms"],
    ["10 ohms", "20 ohms", "30 ohms", "200 ohms"],
    ["Resistor", "Battery", "Switch", "Motor"],

    ["Generator", "Electric motor", "Transformer", "Resistor"],
    ["Changing AC voltage levels", "Storing current", "Generating heat", "Measuring resistance"],
    ["Induction motor", "Stepper motor", "DC motor", "Servo motor"]
]

# Correct answers (option numbers)
answers = [
    1, 2, 1,
    2, 1, 1,
    1, 1, 1,
    2, 3, 1,
    2, 1, 1
]

# Topic index for each question
categories = [
    0, 0, 0,
    1, 1, 1,
    2, 2, 2,
    3, 3, 3,
    4, 4, 4
]


# Calculates percentage
def percentage(score, total):
    return (score / total) * 100


# Main quiz function
def start_quiz():

    score = 0
    topic_scores = [0, 0, 0, 0, 0]
    topic_totals = [0, 0, 0, 0, 0]

    print("\n================================")
    print("       WELCOME TO MECHASENSE")
    print("  MECHATRONICS ASSESSMENT SYSTEM")
    print("================================")

    print("\nTotal questions:", len(questions))
    print("Choose an answer between 1 and 4.")

    # Display questions
    for i in range(len(questions)):

        print("\nQuestion", i + 1)
        print(questions[i])

        for j in range(4):
            print(j + 1, ".", options[i][j])

        # Validate user input
        while True:

            choice = input("Your answer: ")

            if choice in ["1", "2", "3", "4"]:
                choice = int(choice)
                break

            else:
                print("Invalid input. Enter 1, 2, 3 or 4.")

        # Record topic performance
        topic = categories[i]
        topic_totals[topic] += 1

        if choice == answers[i]:

            print("Correct!")
            score += 1
            topic_scores[topic] += 1

        else:
            print("Incorrect!")

    # Calculate overall performance
    result = percentage(score, len(questions))

    print("\n================================")
    print("       PERFORMANCE REPORT")
    print("================================")

    print("Total score:", score, "/", len(questions))
    print("Overall percentage:", round(result, 2), "%")
    # Display performance by topic
    print("\nTOPIC PERFORMANCE")

    for i in range(len(topics)):

        result = percentage(topic_scores[i], topic_totals[i])

        print(topics[i], ":", round(result, 2), "%")

    # Identify strongest and weakest topics
    strongest = 0
    weakest = 0

    for i in range(len(topics)):

        if topic_scores[i] > topic_scores[strongest]:
            strongest = i

        if topic_scores[i] < topic_scores[weakest]:
            weakest = i

    print("\n================================")
    print("       KNOWLEDGE DIAGNOSTICS")
    print("================================")

    print("Strongest area:", topics[strongest])
    print("Weakest area:", topics[weakest])

    # Recommend revision based on performance
    if topic_scores[weakest] == topic_totals[weakest]:
        print("Excellent! You performed equally well across all topics.")

    elif topic_scores[weakest] == 0:
        print("URGENT: Revise", topics[weakest], "before your next assessment.")

    elif topic_scores[weakest] < topic_totals[weakest] / 2:
        print("Recommendation: Prioritise studying", topics[weakest])

    else:
        print("Recommendation: Practise more questions on", topics[weakest])

    # Overall grade
    if result >= 80:
        print("\nGrade: EXCELLENT")

    elif result >= 60:
        print("\nGrade: GOOD")

    elif result >= 50:
        print("\nGrade: FAIR")

    else:
        print("\nGrade: NEEDS IMPROVEMENT")

    print("\nThank you for using MechaSense!")


# Start application
start_quiz()
