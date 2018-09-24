try:
    user_input = int(input("Print a number bewteen 0 and 6? "))
    informative_sentence = "The day of the week is "
    too_high = "The number you chose is to high."
    if user_input == 0:
        print(informative_sentence + "Sunday")
    elif user_input == 1:
        print(informative_sentence + "Monday")
    elif user_input == 2:
        print(informative_sentence + "Tuesday")
    elif user_input == 3:
        print(informative_sentence + "Wednesday")
    elif user_input == 4:
        print(informative_sentence + "Thursday")
    elif user_input == 5:
        print(informative_sentence + "Friday")
    elif user_input == 6:
        print(informative_sentence + "Saturday")
    elif user_input > 6:
        print(too_high)
except:
    print("You did not enter a number...Try again")
    

