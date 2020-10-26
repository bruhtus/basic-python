import requests
url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'

response = requests.get(url)
print(response)
print(response.status_code) #status code, success: 200.
print(response.headers) #headers information.
print(response.text) #gives all the text from the page.
