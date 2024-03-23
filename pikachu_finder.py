from serpapi import GoogleSearch 
params = {
  "engine": "google_reverse_image",
  "image_url": "https://pbs.twimg.com/media/GG_Zyf6aIAAzyJj?format=png&name=900x900",
  "api_key": "placeholder",
  "filter": 0
}

search = GoogleSearch(params)
results = search.get_dict()
inline_images = results["inline_images"]


print(results)
print(len(results))

print(inline_images)


image_sizes = results["image_sizes"]
print(image_sizes)
dic = image_sizes[0]

url = image_sizes[0]['serpapi_link']
url += "&api_key="
url += params['api_key']
print(url)


# import urllib library 
from urllib.request import urlopen 
  
# import json 
import json 

response  = urlopen(url)

data_json = json.loads(response.read()) 
  
# print the json response 
print(data_json) 

images = data_json["images_results"]

for i in images:
    print(i["link"])