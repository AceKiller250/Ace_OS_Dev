from urllib.request import urlopen
  
# import json
import json
# store the URL in url as 
# parameter for urlopen
url = "https://firebasestorage.googleapis.com/v0/b/ace-os-auth.appspot.com/o/settings.json?alt=media&token=5287407f-f879-4680-964d-4932b34df67a"
  
# store the response of URL
response = urlopen(url)
  
# storing the JSON response 
# from url in data
data_json = json.loads(response.read())
  
# print the json response
print(data_json)
