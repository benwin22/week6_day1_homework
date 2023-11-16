import requests 
import requests_cache 
import json 

requests_cache.install_cache('image_cache', backend='sqlite')

# need to fix this
def get_image(search):
    url = "https://google-search72.p.rapidapi.com/imagesearch"

    querystring = {"q": search,"gl":"us","lr":"lang_en","num":"10","start":"0"}

    headers = {
        "X-RapidAPI-Key": "0e9e06a6bdmsh4fb4095b0bc08c5p1bdd16jsnb4eac2ec2419",
        "X-RapidAPI-Host": "google-search72.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()
    # print(data)

    img_url = ""

    if 'items' in data.keys():
           img_url = data['items'][0]['originalImageUrl'] 

    return img_url