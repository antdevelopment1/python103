try:
    user_input = int(input("Print a number bewteen 0 and 6? "))
    commute = "Go to work!!!"
    take_it_easy = "Sleep in!!!"
    
    if user_input == 0:
        print(take_it_easy)
    elif user_input == 1:
        print(commute)
    elif user_input == 2:
        print(commute)
    elif user_input == 3:
        print(commute)
    elif user_input == 4:
        print(commute)
    elif user_input == 5:
        print(commute)
    elif user_input == 6:
        print(take_it_easy)
    elif user_input > 6:
        print("The number you chose is to high.")
except:
    print("You did not enter a number...Try again")

