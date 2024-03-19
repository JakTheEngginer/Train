import random

user_wins = 0
computer_wins = 0
imbang = 0

option = ["Kertas", "Batu", "Gunting"]

while True:
    user_input = input("Kertas/Batu/Gunting or Q or quit").lower()
    if user_input == "Q":
        quit()
    
    if user_input in option:
        continue

    random_number = random.randint(0, 2)
    computer_pick = option[random_number]

    if user_input == "Batu" and computer_pick == "Gunting":
        user_wins += 1
        print("Kamu menang hoki") 
    
    elif user_input == "Kertas" and computer_pick == "Batu":
        user_wins += 1
        print("Kamu menang hoki") 
    
    elif user_input == "Gunting" and computer_pick == "Batu":
        user_wins += 1
        print("Kamu menang hoki")

    elif user_input == computer_pick:
        imbang  += 1

    else:
        computer_wins += 1
        print("Noob")
    
    print("kamu menang", user_wins, "kali" )
    print("computer", computer_wins, "kali" )
    print("kita Imbang",imbang, "kali" )
    print("Selamat Tinggal" )
