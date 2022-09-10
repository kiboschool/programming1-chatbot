from random import randrange

welcoming_msg = """
 1. Tell me about the team
 2. Tell me about the programs
 3. Tell me a programming joke
 4. Exit
 choose a number: """

kibo_info = """Kibo currently offers two programs: the Kibo Math Challenge and Try Kibo. Soon, Kibo will offer a BSc in Computer Science. The Kibo Math Challenge is a virtual 
competition aimed at identifying, engaging, and showcasing senior secondary Maths enthusiasts across Africa. Try Kibo is a beginner-focused online class to explore computing and 
learn to code in a supportive community. The Kibo BSc in Computer Science will let students earn a globally-recognized and accredited Bachelor’s Degree in Computer Science, 
in just under 3 years. It's not enrolling students yet, but check back soon! """

team_info = [["Emeka O", "Community builder, helping people connect. Student, hungry to learn it all. Practicing pythonista."],
             ["George K", "Marketer and entertainer, budding python expert. Loves driving and his family"],
             ["Hamzat O", "Data scientist + operations specialist. Loves to help people, especially if there's something new to find out along the way!"],
             ["Mohammed S", "Sometimes a teacher, always a student. Studying computer science because it's beautiful (and to make awesome stuff!)"],
             ["Keno O", "World traveler, introvert, athlete. Love/hate relationship with academia, but pure love for learning and knowledge (and now Python!)"],
             ["Rob C", "Teacher and coder, finding out new things about computer science every day. Programming for fun on the weekends."],
             ["Ope", "Building products means loving them, even when you know their flaws better than anyone. Kibo CEO, python prowler."]]

jokes = ["Got a B in my computer programming class. Call that a C++",
         "Q: Why did the programmer quit his job? \n A: Because they didn't get arrays"]

input("Hi! I'm the Kibo Team chatbot. How can I help you today? \n Press enter to continue.")

while True:
    answer = input(welcoming_msg)

    if int(answer) == 1:
        team_member = input("1. Emeka O \n 2. George K \n 3. Hamzat O \n 4. Mohammed S \n 5. Keno O \n 6. Rob C \n 7. Ope \n Pick a member: ")
        print(f"More info about {team_info[int(team_member)-1][0]}")

        if int(team_member) == 1:
            print(team_info[int(team_member)-1][1])
            input("Press enter to continue")
        elif int(team_member) == 2:
            print(team_info[int(team_member)-1][1])
            input("Press enter to continue")
        elif int(team_member) == 3:
            print(team_info[int(team_member)-1][1])
            input("Press enter to continue")
        elif int(team_member) == 4:
            print(team_info[int(team_member)-1][1])
            input("Press enter to continue")
        elif int(team_member) == 5:
            print(team_info[int(team_member)-1][1])
            input("Press enter to continue")
        elif int(team_member) == 6:
            print(team_info[int(team_member)-1][1])
            input("Press enter to continue")
        elif int(team_member) == 7:
            print(team_info[int(team_member)-1][1])
            input("Press enter to continue")
        else:
            print("Please choose a member")
        continue

    elif int(answer) == 2:
        print(kibo_info)
        continue

    elif int(answer) == 3:
        rand_num = randrange(len(jokes))
        print(jokes[rand_num])
        continue

    elif int(answer) == 4:
        break

    else:
        print("Please enter a number")
        continue

print("Goodbye for now!")
