from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from ratings.models import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Avg
from django.db.models import Max, Min
from django.db.models import Sum
from django.shortcuts import get_object_or_404
#can use get, post, put and delete here as well!
import requests
import records
import json
import math

# Create your views here.
############# register ###############
@csrf_exempt
def register_user (request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if User.objects.filter(username=username).exists():
            return HttpResponse('User name already exists! Please try again.')
        else:
            user = User.objects.create_user(username = username, password=password, email= email)
            user.save()
            return HttpResponse("Your account has been registered!")
    return HttpResponse("Register page")


#do we need request.session?
############# log in ###############
@csrf_exempt
def logging_in (request):
    if request.method  == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username , password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['username'] = username
                request.session['password'] = password
                # print("logged in!")
                return HttpResponse("You have been logged in!")
            else:
                # print("No account found!")
                return HttpResponse("404. Inactive account!")
        else:
            return HttpResponse("404. Invalid credentials.")
    return HttpResponse('Login page!')
#

############# log out ###############
@csrf_exempt
def logging_out (request):
    if request.method == "POST":
        if request.user.is_authenticated:
            logout(request)
            return HttpResponse("You have been logged out!")
        else:
            return HttpResponse("404. Account must be logged in/registered to be logged out!")
    return HttpResponse("Logout page")

############# list ###############
@csrf_exempt
def list_modules (request):
    the_list = []
    module_list = Module.objects.all().values('mod_code', 'name', 'year', 'semester', 'professor')
    for record in module_list:
        string = Professor.objects.get(id = record['professor']).prof_id + "," + " Professor " + Professor.objects.get(id = record['professor']).first_name + " " + Professor.objects.get(id = record['professor']).last_name
        item = {'Code': record['mod_code'], 'Name': record['name'], 'Year': record['year'],
        'Semester': record['semester'], 'Taught By': string}
        the_list.append(item)
    return HttpResponse(json.dumps(the_list))

############# view rating ###############
@csrf_exempt
def view_ratings (request):
    view_avg_list = []
    ids = Professor.objects.all().values()
    for record in ids:
        id_dict = json.dumps(record)
        loads = json.loads(id_dict)

        p_id = loads['id']
        p_code = loads['prof_id']
        p_name = loads['first_name']
        p_name2 = loads['last_name']

        av_rate = Rating.objects.filter(professor_id=p_id).aggregate(avg=Avg('rating'))['avg']
        a = int (round(av_rate))
        item = {'Professor': "(" + p_code + ") " + p_name + " " + p_name2, 'Average Rating': a}
        view_avg_list.append(item)

    return HttpResponse(json.dumps(view_avg_list))

############# view average rating ###############
@csrf_exempt
def average_ratings (request):

    if request.method  == "POST":
        profcode = request.POST['Prof_input']
        module_code = request.POST['Module_input']

        # view_avg_list2 = []
        p_list = Professor.objects.all().values()

        for record in p_list:
            id_dict2 = json.dumps(record)
            loads2 = json.loads(id_dict2)
            p_id2 = loads2['id']
            p_code2 = loads2['prof_id']
            p_name2 = loads2['first_name']
            p_name22 = loads2['last_name']

            if profcode == p_code2:
                m_list = Module.objects.all().values()
                for item in m_list:
                    m_dict = json.dumps(item)
                    loads3 = json.loads(m_dict)

                    m_id = loads3['id']
                    m_code = loads3['mod_code']
                    m_name = loads3['name']
                    if module_code == m_code:
                        av_rate2 = Rating.objects.filter(professor_id=p_id2).filter(module_id=m_id).aggregate(avg2=Avg('rating'))['avg2']
                        a2 = (math.ceil(av_rate2))
                        return HttpResponse('The rating of Professor (' + p_code2 + ") " + p_name2 +" "+ p_name22 +' in module ' + m_name + " (" + m_code + ") is " + str(a2))
    else:
        return HttpResponse('404. Bad Request! Only Post requests allowed.')
    return HttpResponse('Wrong input! Please check professor/module ID before trying again.')

############# rate ###############
# @login_required
@csrf_exempt
def rate_professor (request):
    if request.user.is_authenticated:
        u_id = request.user.id
        # print(u_id)
        if request.method  == "POST":
            profcode = request.POST['Prof_input']
            module_code = request.POST['Module_input']
            year = request.POST['Year']
            semester = request.POST['Semester']
            rating = request.POST['Rating']

            p_list = Professor.objects.all().values()

            for record in p_list:
                id_dict2 = json.dumps(record)
                loads2 = json.loads(id_dict2)
                p_id2 = loads2['id']
                p_code2 = loads2['prof_id']

                if profcode == p_code2:
                    m_list = Module.objects.all().values()
                    for item in m_list:
                        m_dict = json.dumps(item)
                        loads3 = json.loads(m_dict)

                        m_id = loads3['id']
                        m_code = loads3['mod_code']
                        m_name = loads3['name']
                        if module_code == m_code:
                            Rating.objects.create(professor_id =p_id2 , module_id=m_id , rating=rating, user_id=u_id)
                            return HttpResponse('Rating successfully saved!')
        else:
            return HttpResponse('404. Bad Request! Only Post requests allowed.')
    else:
        return HttpResponse('You must be registered or logged in to proceed!')
    return HttpResponse('Wrong input! Please check professor/module ID before trying again.')


##################################################
###################################################
