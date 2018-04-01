#dependencies
import json
import requests

#url from numbersapi 
url = "http://numbersapi.com/"

#prompt user 
question= ("What type of number information do you want to search for?", "[Trivia, Math, Date, or Year]")
search_type= input(question)

#if conditional to handle if user inputs date
if (search_type.lower() == "date"):
    #collect month and day to search for
    month = input("What month do you want to search for?")
    day = input("What day do you want to search for?")
    #make API call for date number
    date_call= requests.get(f"{url}{month}/{day}/{search_type.lower()}?json").json()
    print(date_call["text"])
#if search type is anything other than date
else:
    #what number users wants to search for
    number = input("What number do you want to search for?")
    #make API call for the number fact
    num_call = requests.get(f"{url}{number}/{search_type.lower()}?json").json()
    print(num_call["text"])




