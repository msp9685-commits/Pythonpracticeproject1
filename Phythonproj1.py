# who want to be millionaire game
while True:
    try:
        cand1 = input("Enter your name: ")
        if cand1 == "" or not cand1.replace(" ", "").isalpha():
            raise ValueError("please enter a valid name")
        print(cand1)
        break
    except ValueError as e:
        print(e)

question2 =["What is the real reason people open the fridge repeatedly?",
"A) To check temperature",
"B) To find food",
"C) Hoping new food appears magically",
"D) To exercise"]

#print question
for i in question2:
    print(i)

#taking input
while True:
    try:
        select = input("Enter an option A/B/C/D: ").upper()
        if select not in ["A", "B", "C", "D"]:
            raise ValueError("Please Enter a Valid option")
        break
    except ValueError as f:
        print(f)
    

if select == "C":
    print("you won 300 rupee\n moving to next question")
else:
    print("you lost")

question3 =["Why do Python programmers prefer dark mode?",
"A) Saves electricity",
"B) Light attracts bugs",
"C) Looks cool",
"D)They are vampires"]

#print question
for i in question3:
    print(i)

#taking input
while True:
    try:
        select = input("Enter an option A/B/C/D: ").upper()
        if select not in ["A", "B", "C", "D"]:
            raise ValueError("Please Enter a Valid option")
        break
    except ValueError as f:
        print(f)
    

if select == "B":
    print("you won 700 rupee\n moving to next question")
else:
    print("you lost")

question4 = ["Why don’t programmers like nature?\n"
"A) Too many bugs",
"B) No WiFi",
"C) No charging",
"D) All of the above"]

#print question
for i in question4:
    print(i)

#taking input
while True:
    try:
        select = input("Enter an option A/B/C/D: ").upper()
        if select not in ["A", "B", "C", "D"]:
            raise ValueError("Please Enter a Valid option")
        break
    except ValueError as f:
        print(f)
    

if select == "D":
    print("you won the game")
else:
    print("you lost")