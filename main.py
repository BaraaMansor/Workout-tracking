import requests
import datetime
import os


APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')


q = input("What did you do in your exercise? ")
url = f"https://trackapi.nutritionix.com/v2/natural/exercise?query=q"


headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

parameters = {
    'query': q
}

response = requests.post(url, headers=headers, json=parameters)

exercises = response.json()
print(exercises)

sheety_url = os.environ.get('SHEET_ENDPOINT')

TOKEN = os.environ.get('TOKEN')
print(TOKEN)

headers = {
    'Authorization': TOKEN
}

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

for exercise in exercises:   
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_response = requests.post(sheety_url, json=sheet_inputs, headers=headers)

    print(sheety_response.text)