import requests

url = 'https://restcountries.eu/rest/v2/all'

response = requests.get(url)
print(response)
print(response.status_code) #success:200
countries = response.json() #use json() method from response object if we are fetching JSON data. for txt, html, xml, and other file formats we can use text.
print(countries[:1])
