#Check whether to pack a jacket or not based on the given temprature

def jacket_query(temprature):
    if temprature < 15:
        print("Wear a jacket, its colder than a vampire's demeanor out there!")
    elif temprature >= 25 and temprature <= 35:
        print('Be Sure to pack a jacket, you dumbass!')
    elif temprature > 35:
        print("Don't pack a jacket. Get a keffiyeh!")

jacket_query(14)
jacket_query(26)
jacket_query(36)