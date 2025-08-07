import requests
# response = requests.get("https://restcountries.com/v3.1/name/germany")
# print(response.json()[0]['capital'][0])
#
# # give me all the objects in the response in a neat format
# for key, value in response.json()[0].items():
#     print(f"{key}: {value}")

# response = requests.get("https://dog.ceo/api/breeds/image/random")
# print(response.json()['message'])

# NASA API

# import requests
#
# url = "https://api.nasa.gov/planetary/apod"
# params = {
#     'api_key': 'XJigElYrfeCGdQzJNjiLyV4LT6S1Vu6vWzYwLkbJ',  # Replace with your API key
#     'date': '2025-08-04'    # Specific date (YYYY-MM-DD)
# }
#
# response = requests.get(url, params=params)
# data = response.json()
# print(f"Title: {data['title']}\nURL: {data['url']}")


import random
from datetime import datetime, timedelta

url = "https://api.nasa.gov/planetary/apod"
DEMO_KEY="XJigElYrfeCGdQzJNjiLyV4LT6S1Vu6vWzYwLkbJ"
# end_date = datetime.now()
# start_date = end_date - timedelta(days=30)
# random_date = start_date + timedelta(days=random.randint(0, 30))
#
# response = requests.get(url, params={
#     'api_key': 'XJigElYrfeCGdQzJNjiLyV4LT6S1Vu6vWzYwLkbJ',
#     'date': random_date.strftime('%Y-%m-%d')
# })
# print(response.json()['url'])



# from PIL import Image
# from io import BytesIO
#
# response = requests.get(url, params={'api_key': 'DEMO_KEY'})
# img_url = response.json()['url']
#
# if img_url.endswith(('.jpg', '.png')):
#     img_data = requests.get(img_url).content
#     img = Image.open(BytesIO(img_data))
#     (img.show

# APOD video
# data = requests.get(url, params={'api_key': 'DEMO_KEY'}).json()
#
# if data['media_type'] == 'video':
#     print(f"Video URL: {data['url']}")
#     # For YouTube embeds:
#     if 'youtube' in data['url']:
#         video_id = data['url'].split('/')[-1]
#         print(f"Embed: https://www.youtube.com/embed/{video_id}")

import requests
import webbrowser

API_KEY="XJigElYrfeCGdQzJNjiLyV4LT6S1Vu6vWzYwLkbJ"
URL=f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

response = requests.get(URL)
if response.status_code == 200:
    data= response.json()
    print(f"Title:", data['title'])
    print(f"Explanation:", data['explanation'])
    print(f"Date:", data['date'])
    print(f"URL:", data['url'])

    webbrowser.open_new_tab(data['url'])