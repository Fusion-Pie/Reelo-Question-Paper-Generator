from django.shortcuts import render, HttpResponse
import requests, json, time
from .models import QuestionsDB

# Create your views here.
def home(request):

    for diff in ['easy', 'hard', 'medium']:
        time.sleep(10)
        # Sports --> 21; Geography --> 22; Science and Nature --> 17; General Knowledge --> 9
        # Science Computers --> 18; Maths --> 19; Animals --> 27
        for category in [21, 22, 17, 9, 18, 19, 27]:
            time.sleep(10)

            done = diff + ' ' + str(category)
            
            base_url = f'https://opentdb.com/api.php?amount=50&category={category}&difficulty={diff}'

            response = json.loads(requests.get(base_url).text)['results']

            # Getting the reponse from the api so that it can be directly run in the django and then can be used 
            # to fill up the db
            for quest in response:
                QuestionsDB(question = quest['question'],category = quest['category'], correctAns = quest['correct_answer'], incorrectAns = quest['incorrect_answers'],
                            difficulty = quest['difficulty'], type = quest['type']).save()
            
            print(done)

    # https://opentdb.com/api_config.php
    return HttpResponse("This is the page")