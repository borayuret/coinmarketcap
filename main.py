import requests
import json


api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency"
                           "/listings/latest?start=1&limit=5&convert=USD&"
                           "CMC_PRO_API_KEY=f1e4d2c9-ca98-4890-8b29-70ee91a81a86")

result = json.loads(api_request.content)

print(result)

