# import the package
from PyBurprestapi import burpscanner

# setup burp connection
host = 'http://127.0.0.1:1337/'

# Burp API key
api_key = '<your key>'

# importing host and key
burp_api = burpscanner.BurpApi(host, api_key)
#
data = '{"application_logins":[{"password":"<your password>","type":"UsernameAndPasswordLogin","username":"<your username>"}],"urls":["<your url>"]}'

# scan Launch
response = burp_api.scan(data)

# Get the response message
print(response.message)

# Get response header (Scan ID found in Location)
print(response.response_headers)