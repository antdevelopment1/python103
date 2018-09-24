def another_chance():
    try:
        user_input = int(input("Print a number bewteen 0 and 6? "))
        days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        returned_day = days_of_week[user_input]
        print("The day of the week is %s" % returned_day)
    except:
        print("You did not enter a valid number between 1 and 6...Try again")
        another_chance()
    
another_chance()

