import random

# Respostas a partir de um Banco de respostas
def chatbot_level_7():
    print("\nTo exit write '/exit'")

    bank = ["Today is Monday, the 8th of November","Lisbon is the capital of Portugal","To exit write '/exit'","IST is a portuguese university","Football is the most popular sport in the world","HackerSchool has a lot of great projects","The sun is shining"]

    chat = input("\nUser: ")

    while chat != "/exit":
        if "day" in chat:
            print("\nBot: " + bank[0])
        elif "Lisbon" in chat:
            print("\nBot: " + bank[1])
        elif "exit" in chat:
            print("\nBot: " + bank[2])
        elif "IST" in chat:
            print("\nBot: " + bank[3])
        elif "sport" in chat:
            print("\nBot: " + bank[4])
        elif "HackerSchool" in chat:
            print("\nBot: " + bank[5])
        elif "weather" in chat:
            print("\nBot: " + bank[6])
        else:
            rand = random.choice(bank)
            print("\nBot: " + rand)
        chat = input("\nUser: ")

    print("\nUser has left the chat...")
    return


# Respostas de acordo com as mensagens e palavras específicas
def chatbot_level_5():
    print("\nTo exit write '/exit'")
    
    bank = ["Today is Monday, the 8th of November","Lisbon is the capital of Portugal","To exit write '/exit'","IST is a portuguese university","Football is the most popular sport in the world","HackerSchool has a lot of great projects","The sun is shining"]
    
    chat = input("\nUser: ")

    while chat != "/exit":
        if "day" in chat:
            print("\nBot: " + bank[0])
        elif "Lisbon" in chat:
            print("\nBot: " + bank[1])
        elif "exit" in chat:
            print("\nBot: " + bank[2])
        elif "IST" in chat:
            print("\nBot: " + bank[3])
        elif "sport" in chat:
            print("\nBot: " + bank[4])
        elif "HackerSchool" in chat:
            print("\nBot: " + bank[5])
        elif "weather" in chat:
            print("\nBot: " + bank[6])
        else:
            print("\nBot: <no familiar words detected>")
        chat = input("\nUser: ")
    
    print("\nUser has left the chat...\n")
    return


# Respostas aleatórias
def chatbot_level_4():
    print("\nTo exit write '/exit'")

    bank = ["Today is Monday, the 8th of November","Lisbon is the capital of Portugal","To exit write '/exit'","IST is a portuguese university","Football is the most popular sport in the world","HackerSchool has a lot of great projects","The sun is shining"]
    
    chat = input("\nUser: ")

    while chat != "/exit":
        rand = random.choice(bank)
        print("\nBot: " + rand)
        chat = input("\nUser: ")

    print("\nUser has left the chat...\n")
    return



def chatbot():
    print("\n-------------------------\n|                       |\n|    · ChatBot ·        |\n|                       |\n|  1 - Random (4)       |\n|                       |\n|  2 - Specific (5)     |\n|                       |\n|  3 - Random Bank (7)  |\n|                       |\n|  4 - Login Menu       |\n|                       |\n-------------------------\n")
    option = input("Type the option's number: ")

    if option == '1':
        chatbot_level_4()
        chatbot()
        return
    elif option == '2':
        chatbot_level_5()
        chatbot()
        return
    elif option == '3':
        chatbot_level_7()
        chatbot()
        return
    elif option == '4':
        return
    else:
        print("\n<ERROR> Unknown Option\n")
        chatbot()
    return