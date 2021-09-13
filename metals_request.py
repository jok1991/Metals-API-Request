import requests


base_currency = 'XAU'
symbol = 'USD' 
endpoint = 'latest'
access_key = 'KEY ON EMAIL HERE!'

response = requests.get(
    'https://www.metals-api.com/api/'+endpoint+'?access_key='+access_key+'&base='+base_currency+'&symbols='+symbol)

if response.status_code != 200:
    # NOT RIGHT
    raise ApiError('GET /'+endpoint+'/ {}'.format(response.status_code))

data = response.json()

for key, value in data.items():
    print('{}: {}'.format(key, value))

print("-------------------")

print("Get price as tuple")
price = data["rates"]["USD"]
print(price)