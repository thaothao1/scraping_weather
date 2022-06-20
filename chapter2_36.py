import requests
url = "http://www.webscrapingfordatascience.com/basichttp/"
r = requests.get(url)

# which HTTP status code did we get back from the server?
print("status code", r.status_code)
# what is the textual status code ?
print("reason", r.reason)
# what were the HTTP response headers?
print("headers", r.headers)
# the request information is saved as a python object in r.request:
print("request.headers", r.request.headers)
# the HTTP response content:
print("text", r.text)
