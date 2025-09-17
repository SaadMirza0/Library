
import random
question = [
    "Q: What is the capital city of Pakistan?",#0
    "Q: What is the national animal of Pakistan?",#1
    "Q: Which is the most populous province of Pakistan?",#2
    "Q: What is the national game of Pakistan?",#3
    "Q: In which year did Pakistan win the Cricket World Cup?",#4
    "Q: Which is the highest peak in Pakistan?",#5
    "Q: Which country is known as the \"Groom\" of Pakistan?",#6
    "Q: Which famous river flows through Lahore?",#7
    "Q: What is the national fruit of Pakistan"#8
    ]
    
total_prize = 0
selected = random.sample(question, 5)

def question_picker(a):
    prize = 0
    match a:
        case _ if a == question[0]: #1
            print(question[0])
            ans = input("Enter any option :\n A:Islamabad \n B:Karachi \n C:Peshawar \n D:Quetta ").upper()
            if (ans == "A"):
                print("Right Answer")
                prize += 100
                print("You got",prize,"in prize")
            else:
                print("Wrong answer Good luck next time")
        case _ if a == question[1]:#2
            print(question[1])
            ans = input("Enter any option :\n A:Goat \n B:Tiger \n C:Bear \n D:Markhor \n").upper()
            if (ans == "D"):
                print("Right Answer")
                prize += 100
                print("You got",prize,"in prize")
            else:
                print("Wrong answer")
        case _ if a == question[2]:#3
            print(question[2])
            ans = input("Enter any option :\n A:Punjab \n B:Sindh \n C:Balochistan \n D:KPK ").upper()
            if (ans == "A"):
                print("Right Answer")
                prize += 100
                print("You got",prize,"in prize")
            else:
                print("Wrong answer")
        case _ if a == question[3]:#4
            print(question[3])
            ans = input("Enter any option :\n A:Cricket \n B:Field Hockey  \n C:Football \n D:Badminton ").upper()
            if (ans == "B"):
                print("Right Answer")
                prize += 100
                print("You got",prize,"in prize")
            else:
                print("Wrong answer")
        case _ if a == question[4]:#5
            print(question[4])
            ans = input("Enter any option :\n A:1915 \n B:1992 \n C:2025 \n D:2005 ").upper()
            if (ans == "B"):
                print("Right Answer")
                prize += 100
                print("You got",prize,"in prize")
            else:
                print("Wrong answer")
        case _ if a == question[5]:#6
            print(question[5])
            ans = input("Enter any option :\n A:Nanga Parbat \n B:Broad Peak \n C:Gasherbrum \n D:K2 ").upper()
            if (ans == "D"):
                print("Right Answer")
                prize += 100
                print("You got",prize,"in prize")
            else:
                print("Wrong answer")
        case _ if a == question[6]:#7
            print(question[6])
            ans = input("Enter any option :\n A:Islamabad \n B:Lahore \n C:Rawalpindi \n D:Karachi ").upper()
            if (ans == "D"):
                print("Right Answer")
                prize += 100
                print("You got",prize,"in prize")
            else:
                print("Wrong answer")        
        case _ if a == question[7]:#8
            print(question[7])
            ans = input("Enter any option :\n A:Chanab \n B:Jehlum River \n C:Ravi River \n D:Satlej ").upper()
            if (ans == "C"):
                print("Right Answer")
                prize += 100
                print("You got",prize,"in prize")
            else:
                print("Wrong answer")
        case _ if a == question[8]:#9
            print(question[8])
            ans = input("Enter any option :\n A:Mango \n B:Apple \n C:Orange \n D:PomeGranate ").upper()
            if (ans == "A"):
                print("Right Answer")
                prize += 100
                print("You got",prize,"in prize")
            else:
                print("Wrong answer")
    return prize
    
for i in selected:
     total_prize += question_picker(i)
     
print(total_prize)
