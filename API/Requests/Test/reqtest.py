import requests

#pip install requests

#https://docs.python-requests.org/en/master/
#https://docs.python-requests.org/en/latest/
#https://www.coingecko.com/en/api/documentation
#https://github.com/man-c/pycoingecko

response = requests.get("https://api.coingecko.com/api/v3/ping")

print(response.status_code)
print(response.headers['content-type'])
print(response.encoding)
print(response.text)

#if response == 200
#Status = OK
#Else
#300 || 400
#Status = Something bad