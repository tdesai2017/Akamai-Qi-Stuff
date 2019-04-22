from django.shortcuts import render
from django.http import HttpResponse
from quest_extension.models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.utils.http import urlencode


def home(request):
    return render(request, 'quest_extension/home.html')
# Create your views here.

def quest_create(request):
    """creates a quest"""
    
    if request.method == 'POST':
        # form was submitted
        form = QuestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/quest/admin_quest_page/' + request.POST['quest_name'])
    else:
        form = QuestForm()
    return render(request, 'quest_extension/test.html', {'form': form})


def create_fr_question(request, name):
    if request.method  == 'POST':
        #for was busmitted
        question_form = QuestionForm(request.POST)
        ans_form = CorrectAnswerForm(request.POST)
        if question_form.is_valid() and ans_form.is_valid():
            #quest_name = request.GET.urlencode().split('=')[1]
            quest = Quest.objects.get(quest_name=name)
            bbb = question_form.save(commit=False)
            bbb.question_type = 'FR'
            
            if not bbb.question_text[len(bbb.question_text)-1] == '?':
                bbb.question_text += '?'


            bbb.quest = quest
            bbb.save()
            question_id = bbb.id

            ccc = ans_form.save(commit=False)
            ccc.question = Question.objects.get(id=question_id)
            ccc.save()
            
            return HttpResponseRedirect('/quest/admin_quest_page/' + name)
    else:
        form = QuestionForm()
        ans_form = CorrectAnswerForm()
    return render(request, 'quest_extension/fr_question_form.html', {'q_form' : form,
                                                         'ans_form' : ans_form})


def create_mc_question(request, name):
    if request.method  == 'POST':
        #for was submitted
        question_form = QuestionForm(request.POST)
        ans_form = CorrectAnswerForm(request.POST)
        wrong_ans_form = WrongAnswerForm(request.POST)
        if question_form.is_valid() and ans_form.is_valid() and wrong_ans_form.is_valid():
            #quest_name = request.GET.urlencode().split('=')[1]
            quest = Quest.objects.get(quest_name=name)
            bbb = question_form.save(commit=False)
            bbb.quest = quest
            bbb.save()

            if not bbb.question_text[len(bbb.question_text)-1] == '?':
                bbb.question_text += '?'

            #text = form.cleaned_data['question_text']

            question_id = bbb.id
            ccc = ans_form.save(commit=False)
            ccc.question = Question.objects.get(id=question_id)
            ccc.save()

            list_of_wrong_answers = wrong_ans_form.cleaned_data['incorrect_answer_text'].split('\n')

            for wrong_answer in list_of_wrong_answers:
                ddd = IncorrectAnswer(question=Question.objects.get(id=question_id), incorrect_answer_text=wrong_answer)
                ddd.save()

            
            return HttpResponseRedirect('/quest/admin_quest_page/' + name)
    else:
        question_form = QuestionForm(initial={'type': 'MC',})
        ans_form = CorrectAnswerForm()
        mc_form = WrongAnswersForm()
    return render(request, 'quest_extension/mc_question_form.html', {'q_form' : question_form,
                                                                     'ans_form' : ans_form,
                                                                     'mc_form' : mc_form})


# def choose_question_type(request, name):
#     return render(request, 'quest_extension/choose_question.html', {'name': name})



# def quest_home(request):
#     user = User.objects.get(ldap='edli')
#     curr_quest = user.current_quest
#     return render(request, 'quest_extension/index.html', {'user': user.first_name + ' ' + user.last_name,
#                                                           'curr_quest' : curr_quest.quest_name,
#                                                           'points' : user.points,
#                                                           'question' : Question.objects.get(quest_id=curr_quest.quest_id).question_text})


def admin_home(request):


    if request.method == 'POST':
        post_request = request.POST
        quest_form = QuestForm(post_request)
        print(post_request)
        if 'quest_description' in request.POST and 'quest_points_earned' in request.POST and 'quest_name' in request.POST:
           #make sure to make quest_name unique
            if quest_form.is_valid():
                quest_form.save()
                return HttpResponseRedirect('/quest/admin_quest_page/' + post_request['quest_name'])
                #return HttpResponseRedirect('/quest/choose-mc-or-fr/' + post_request['quest_name'])

    #user = User.objects.get(ldap='edli')
    quests = Quest.objects.all()
    quest_form = QuestForm()
    context = {'quests':quests, 'quest_form': quest_form}
    return render(request, 'quest_extension/admin_home.html', context)

def admin_quest_page(request, name):

    current_quest = Quest.objects.get(quest_name = name)
    list_of_questions = Question.objects.filter(quest = current_quest)
    fr_input_form = TakeInFreeResponseForm

    format = {}
    for question in list_of_questions:
        wrong_answers = IncorrectAnswer.objects.filter(question = question)
        format[question] = wrong_answers

    context = {'current_quest': current_quest, 'format': format, 'fr_input_form': fr_input_form}
    return render(request, 'quest_extension/admin_quest_page.html', context)

def user_home(request, ldap):

    user = User.objects.get(user_ldap= ldap)
    quests = Quest.objects.all()
    quest_form = QuestForm()
    context = {'quests':quests, 'quest_form': quest_form, 'user': user}
    return render(request, 'quest_extension/user_home.html', context)
    

def user_quest_page(request, ldap, name):

    current_quest = Quest.objects.get(quest_name = name)
    list_of_questions = Question.objects.filter(quest = current_quest)
    fr_input_form = TakeInFreeResponseForm

    format = {}
    for question in list_of_questions:
        wrong_answers = IncorrectAnswer.objects.filter(question = question)
        format[question] = wrong_answers

    context = {'current_quest': current_quest, 'format': format, 'fr_input_form': fr_input_form, 'ldap': ldap}
    return render(request, 'quest_extension/user_quest_page.html', context)