import requests
import ast

def get_picture():
  url = "https://dog.ceo/api/breeds/image/random"
  response = requests.get(url)

  if response.status_code == 200:
    content = response.content
    dict_str = content.decode("UTF-8")
    dict_str  = ast.literal_eval(dict_str)
    picture = dict_str["message"]
    return picture
  else:
    return "not avaliable picture"