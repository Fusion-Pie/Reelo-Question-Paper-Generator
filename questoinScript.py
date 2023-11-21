import requests
import json

base_url = f'https://opentdb.com/api.php?amount=1&category=9&difficulty=easy'

response = json.loads(requests.get(base_url).text)


# Getting the reponse from the api so that it can be directly run in the django and then can be used 
# to fill up the db
print(response['results'][0]['question'])

# https://opentdb.com/api_config.php