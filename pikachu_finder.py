from serpapi import GoogleSearch 
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen 
import json 

def source_image(image_url):
  print(image_url)

  params = {
    "engine": "google_reverse_image",
    "image_url": image_url,
    "api_key": "852564d05052e29ed6b66ab33277484004f9dd4e4b41aec7d4ff7d1c3e309497",
    "filter": 0
  }

  search = GoogleSearch(params)
  results = search.get_dict()
  print(results)
  #inline_images = results["inline_images"]


  print(results)
  print(len(results))

  #print(inline_images)
  image_sizes = results["image_sizes"]
  print(image_sizes)
  dic = image_sizes[0]



  url = image_sizes[0]['serpapi_link']
  url += "&api_key="
  url += params['api_key']
  print(url)



  response  = urlopen(url)

  data_json = json.loads(response.read()) 
    
  # print the json response 
  print(data_json) 

  images = data_json["images_results"]

  links = []
  for i in images:
      links.append(i["link"])
  links = links[::-1]
  #((artist|credit( to)?|twt|twitter|twi|ig|instagram|insta|op|facebook|fb|pixiv):?\s*@?([^\s])+


  #regex = "((artist|owner|credit( to)?|twt|twitter|twi|ig|instagram|insta|op|facebook|fb|pixiv):?\s*@?([^\s])+)"
  regex = "((artist|owner|credit( to)?|twt|twitter|twi|ig|instagram|insta|op|facebook|fb|pixiv):?\s*@?([^\s]+))+"
  driver = webdriver.Chrome()

  texts = []
  matches = []
  for i in links:
      driver.get(i)
      data = driver.page_source
      soup = BeautifulSoup(data)
      txt = soup.prettify()
      texts.append(txt)
      x = re.findall(regex, txt)
      matches.append(x)

  print(matches)
  for i in range(len(links)):
      print(i)
      print(links[i])
  print(texts[0])
  regex = "(\s(artist|owner|credit( to)?|twt|twitter|twi|ig|instagram|insta|op|facebook|fb|pixiv):?\s+@?([\w_]+))+"
  #made there be a space at the start of the word bc of things like "top: 0"
  #changed the artists name from non white space chars to alphanumeric plus underscores, bc of config = ...
  #
  for i in range(len(texts)):
      x = re.findall(regex, texts[i])
      print(i)
      if len(x) > 0:
          print(x)
          return x[0][3]
