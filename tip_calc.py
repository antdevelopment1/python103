try: 
    total = int(input("What is the total bill amount? $"))
    quality_service_rating = input("Was you service good, fair, or bad? ").lower()
    message = "Your total bill including tip is $"
    great = "We are glad that you liked your service."
    so_so = "We want to improve. Let us know what we can do to make your service great."
    awful = "We are so sorry you didn't like your service."
    if quality_service_rating == 'good':
        new_total = total + (total * .20)
        review = great
    elif quality_service_rating == 'fair':
        new_total = total + (total * .15)
        review = so_so
    elif quality_service_rating == 'bad':
        new_total = total + (total * .10)
        review = awful
    elif quality_service_rating != 'good' or quality_service_rating != 'fair' or quality_service_rating != 'bad':
        print('Something seems of with your quality service rating. Please follow specified instructions.')
    print(message, "{:.2f}".format(new_total), review)
except:
    print("Some info seems off. Please enter the specified values in the instructions.")