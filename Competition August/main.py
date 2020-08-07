# We are adding an application that adds personalized data to a list of general data
import pandas as pd
import matplotlib.pyplot as plt

is_guessing = False
get_data = True

file = open("Food Dataset Generic.csv", 'a')
file.close()



while get_data:
    file = open('Food Dataset Generic.csv', 'a')
    need_cal = True

    df_dict = []
    df = pd.read_csv('Food Dataset Generic.csv')
    for index, row in df.iterrows():
        d = row.to_dict()
        df_dict.append(d)

    new_food = input("What new food did you try out? ")

    for i in range(len(df_dict)):
        if new_food == df_dict[i]["Food and Serving"]:
            cal = df_dict[i]["Calories"]
            cal = str(cal)
            need_cal = False
            break

    if need_cal:
        print("\nCalories not found in our database.\n")
        cal = input("Calories (estimated) of food? ")

    typeoffood = input("Type of cuisine / food: ")

    tod = input("Time of day eating food (7:30 pm would be 19.5)")

    mood = input("Reason for eating food? (Hungry, bored, etc.) ")

    inp = new_food + ',' + cal + ',' + typeoffood + ',' + tod + ',' + mood

    file.write(inp)
    file.write("\n")
    file.close()

    get = input("End training? ")

    if get == 'Yes' or get == 'yes':
        get_data = False
        is_guessing = True

import requests
import json


def get_prediction(data={
        "Calories": 20,
        "Food Type": "Veg",
        "TOD": "Generic", 
        "Feeling": "Generic"
}):
    url = 'https://l47syleshe.execute-api.us-east-1.amazonaws.com/Predict/cdebab45-adf1-4d20-9efa-db56fdf0b37b'
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r, '_content').decode("utf-8")
    return response


while is_guessing:
    calories_input = input(
        "\n\nHow many calories are you looking for? (If you don't care, put 200.) "
    )
    food_type = input("Type of food? If you want random, put generic: ")
    timeofday = input("Time of day: ")
    feeling = input("How are you feeling? ")
    data = {
        "Calories": float(calories_input),
        "Food Type:": food_type,
        "TOD": timeofday,
        "Feeling": feeling
    }
    ret = json.loads(get_prediction(data=data))
    ret = json.loads(ret["body"])
    ret = ret["predicted_label"]
    print(ret)

    guess = input("Still want to guess? ")
    if guess == 'No' or guess == "no":
        is_guessing = False
