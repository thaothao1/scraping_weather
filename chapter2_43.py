import requests
from urllib.parse import unquote


class NonEncodedSession(requests.Session):
    # Override the default send method
    def send(self, *a, **kw):
        # Revert the encoding which was applied
        a[0].url = unquote(a[0].url)
        return requests.Session.send(self, *a, **kw)


my_requests = NonEncodedSession()

url = 'http://www.example.com/?spaces |pipe'
r = my_requests.get(url)
print(r.url)
