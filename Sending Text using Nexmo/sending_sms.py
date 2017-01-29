import urllib
import urllib2

params = {
    'api_key': '#YourApiKey',
    'api_secret': '#YourAPISecret',
    'to': '918587099540',
    'from': '918587099540',
    'text': 'Hello from Nexmo'
}

url = 'https://rest.nexmo.com/sms/json?' + urllib.urlencode(params)

request = urllib2.Request(url)
request.add_header('Accept', 'application/json')
response = urllib2.urlopen(request)
