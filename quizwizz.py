# Basic Python Program

# Taking input from the user
name = input("Enter your name: ")
coo=input("Enter your nationality:-" )
age = int(input("Enter your age: "))

# Simple Cricket Quiz in Python

score = 0

print("Welcome to the Cricket Quiz!\n")

# Question 1
print("1. Who is known as the 'God of Cricket'?")
print("a) Virat Kohli\nb) Sachin Tendulkar\nc) MS Dhoni\nd) Rohit Sharma")
answer1 = input("Your answer: ").strip().lower()
if answer1 == 'b' or answer1 == 'sachin tendulkar':
    score += 1

# Question 2
print("\n2. How many players are there in a cricket team?")
print("a) 10\nb) 11\nc) 12\nd) 9")
answer2 = input("Your answer: ").strip().lower()
if answer2 == 'b' or answer2 == '11':
    score += 1

# Question 3
print("\n3. Which country won the ICC Cricket World Cup in 2011?")
print("a) India\nb) Australia\nc) England\nd) Sri Lanka")
answer3 = input("Your answer: ").strip().lower()
if answer3 == 'a' or answer3 == 'india':
    score += 1


# Question 4
print("\n4. Who won the orange cap of IPL 2008?")
print("a) Mitchell Marsh\nb) Shaun Marsh\nc) Yusuf Pathan\nd) MS Dhoni")
answer3 = input("Your answer: ").strip().lower()
if answer3 == 'b' or answer3 == 'Shaun Marsh':
    score += 1


# Question 5
print("\n5. Who was the Most Valuable Player of IPL 2017?")
print("a) Krunal Pandya\nb) Steve Smith\nc) Ben Stokes\nd) MS Dhoni")
answer3 = input("Your answer: ").strip().lower()
if answer3 == 'c' or answer3 == 'Ben Stokes':
    score += 1



# Question 6
print("\n6. Who was the inaugral World Cup winner?")
print("a) West Indies\nb) Australia\nc) India\nd) England")
answer3 = input("Your answer: ").strip().lower()
if answer3 == 'a' or answer3 == 'West Indies':
    score += 1


# Question 7
print("\n7. One of the two new teams playing in IPL 2017 were Gujarat and  ?")
print("a) Kerala\nb) Lucknow\nc) Pune\nd)Ranchi ")
answer3 = input("Your answer: ").strip().lower()
if answer3 == 'c' or answer3 == 'Pune':
    score += 1

# Question 8
print("\n8. I have played for DD,KXIP,MI,PWI,SRH. Who am I?")
print("a) Krunal Pandya\nb) Steve Smith\nc)Yuvraj Singh\nd) MS Dhoni")
answer3 = input("Your answer: ").strip().lower()
if answer3 == 'c' or answer3 == 'Yuvraj Singh':
    score += 1

# Question 9
print("\n9. Who was the captain of West Indies in 1983 World Cup ?")
print("a) Viv Richards \nb) Joel Garner\nc) Clive Lloyd\nd) Kapil Dev")
answer3 = input("Your answer: ").strip().lower()
if answer3 == 'c' or answer3 == 'Clive Lloyd':
    score += 1

# Question 10
print("\n10. Who was the purple cap winner of IPL 2016?")
print("a) Bhuvneshwar Kumar \nb) Yuzvendra Chahal\nc) Ben Stokes\nd) Rashid Khan")
answer3 = input("Your answer: ").strip().lower()
if answer3 == 'a' or answer3 == 'Bhuvneshwar Kumar':
    score += 1


# Final Score
print(f"\nYour final score is: {score}/10")
if score == 10:
    print("Excellent! You're a cricket champ!")
elif score == 9:
    print("Good job! You know your cricket.")
elif score == 8:
    print("Bravo, you are entering into the wolrd of cricket.")
else:
    print("Keep learning. Cricket has a lot to offer!")
