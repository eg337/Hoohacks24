from serpapi import GoogleSearch 

params = {
  "engine": "google_reverse_image",
  "image_url": "https://pbs.twimg.com/media/GG_Zyf6aIAAzyJj?format=png&name=900x900",
  "api_key": "0f26d71770473fb70138e4e05cd456fc4b3335761522c23d08e0fc31fa3ec593"
}

search = GoogleSearch(params)
results = search.get_dict()
inline_images = results["inline_images"]