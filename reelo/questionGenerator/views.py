from django.shortcuts import render, HttpResponse
from .models import QuestionsDB

# Libraries used for the purpose of the 
# import requests, json, time

# Create your views here.
def home(request):
    if request.method == 'POST':
        if request.POST['btn_name'] == 'Get Started !':
            return render(request, 'userInput.html')
    else:
        return render(request, 'base.html')
    

def generatePaper(request):
    if request.method == 'POST':
        
        if request.POST['btn_name'] == 'Generate Paper':
                
                question_list = []

                for diff in ['easy', 'medium', 'hard']:

                    no_of_ques = round((int(request.POST['no_of_ques']) * int(request.POST['percent_of_' + diff])) / 100)

                    question_list.extend(QuestionsDB.objects.filter(difficulty = diff).order_by('?')[:no_of_ques])


                # print(question_list)
                
                # content = ''

                # for obj in question_list:
                #     content += obj.question

                return render(request, 'questionPaper.html', context = {'questions' : question_list })



# Script for populating the db

    # for diff in ['easy', 'hard', 'medium']:
    #     time.sleep(10)
    #     # Sports --> 21; Geography --> 22; Science and Nature --> 17; General Knowledge --> 9
    #     # Science Computers --> 18; Maths --> 19; Animals --> 27
    #     for category in [21, 22, 17, 9, 18, 19, 27]:
    #         time.sleep(10)

    #         done = diff + ' ' + str(category)
            
    #         base_url = f'https://opentdb.com/api.php?amount=50&category={category}&difficulty={diff}'

    #         response = json.loads(requests.get(base_url).text)['results']

    #         # Getting the reponse from the api so that it can be directly run in the django and then can be used 
    #         # to fill up the db
    #         for quest in response:
    #             QuestionsDB(question = quest['question'],category = quest['category'], correctAns = quest['correct_answer'], incorrectAns = quest['incorrect_answers'],
    #                         difficulty = quest['difficulty'], type = quest['type']).save()
            
    #         print(done)

    # https://opentdb.com/api_config.php