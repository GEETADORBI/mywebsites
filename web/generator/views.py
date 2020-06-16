# -*- coding: utf-8 -*-

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
# import json to load json data to python dictionary
import json
import datetime
from .forms import NameForm
# urllib.request to make a request to api
import urllib.request
def home(request):
    #return render(request,'generator/home.html',)
    if request.method == 'POST':

        city = request.POST['city']
        ''' api key might be expired use your own api_key 
            place api_key in place of appid ="your_api_key_here "  '''

        # source contain JSON data from API
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=8ced9d7feb00d801601b6c672c018b00&units=metric').read()

        # converting JSON data to a dictionary
        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ','
                              + str(list_of_data['coord']['lat']),
                "temp": str(list_of_data['main']['temp']) +'°' +'C',
                 "name": str(list_of_data['name']),
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                    }
        print(data)
    #else:
        #if city is None:
           # return render(request, 'generator/current.html', {'form': NameForm(), 'error': 'enter city name'})
    else:
            data = {}
    return render(request, "generator/home.html", data)
def signup(request):
    if request.method=='GET':
        return render(request,'generator/signup.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user= User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('current')

            except IntegrityError:
                return render(request, 'generator/signup.html',{'form': UserCreationForm(), 'error': 'user name is taken'})

        else:
            return render(request, 'generator/signup.html', {'form': UserCreationForm(),'error':'passwords didnot matches'})

def loginuser(request):
    if request.method=='GET':
        return render(request,'generator/login.html',{'form':AuthenticationForm()})
    else:
        user= authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'generator/login.html',{'form':AuthenticationForm(),'error':'username and password didnot match'})
        else:
            login(request, user)
            return redirect('current')

def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')


def current(request):
    if request.method == 'POST':

        city = request.POST['city']
        ''' api key might be expired use your own api_key 
            place api_key in place of appid ="your_api_key_here "  '''

        # source contain JSON data from API
        source1 = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=5250d124bb33c76964c897b52be44dad&units=metric').read()
        # converting JSON data to a dictionary
        list_of_data1 = json.loads(source1)
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/forecast?q=' + city + '&appid=8ced9d7feb00d801601b6c672c018b00&units=metric').read()

        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
                "country_codee": str(list_of_data1['sys']['country']),
                "coordinatee": str(list_of_data1['coord']['lon']) + ', '
                              + str(list_of_data1['coord']['lat']),
                "tempp": str(list_of_data1['main']['temp']) + '°'+'C',
                 "namee": str(list_of_data1['name']),
                "pressuree": str(list_of_data1['main']['pressure']),
                "humidityy": str(list_of_data1['main']['humidity']),
                "windd": str(list_of_data1['wind']['speed']),
                "descriptionn" : str(list_of_data1['weather'][0]['description']),



            "humidity": str(list_of_data['list'][0]['main']['humidity']),
            "temp": str(list_of_data['list'][0]['main']['temp']) + '°'+"C",
             "date": str(list_of_data['list'][0]['dt_txt']),
            "weather": str(list_of_data['list'][0]['weather'][0]['description']),
            "icon": str(list_of_data['list'][0]['weather'][0]['icon']),

            "humidity1": str(list_of_data['list'][1]['main']['humidity']),
            "temp1": str(list_of_data['list'][1]['main']['temp'])+ '°'+ "C",
            "date1": str(list_of_data['list'][1]['dt_txt']),
            "weather1": str(list_of_data['list'][1]['weather'][0]['description']),
            "icon1": str(list_of_data['list'][1]['weather'][0]['icon']),

            "humidity2": str(list_of_data['list'][2]['main']['humidity']),
            "temp2": str(list_of_data['list'][2]['main']['temp']) + '°'+ "C",
            "date2": str(list_of_data['list'][2]['dt_txt']),
            "weather2": str(list_of_data['list'][2]['weather'][0]['description']),
            "icon2": str(list_of_data['list'][2]['weather'][0]['icon']),

            "humidity3": str(list_of_data['list'][3]['main']['humidity']),
            "temp3": str(list_of_data['list'][3]['main']['temp']) + '°'+ "C",
            "date3": str(list_of_data['list'][3]['dt_txt']),
            "weather3": str(list_of_data['list'][3]['weather'][0]['description']),
            "icon3": str(list_of_data['list'][3]['weather'][0]['icon']),

            "humidity4": str(list_of_data['list'][4]['main']['humidity']),
            "temp4": str(list_of_data['list'][4]['main']['temp']) + '°'+ "C",
            "date4": str(list_of_data['list'][4]['dt_txt']),
            "weather4": str(list_of_data['list'][4]['weather'][0]['description']),
            "icon4": str(list_of_data['list'][4]['weather'][0]['icon']),

            "weather5": str(list_of_data['list'][5]['weather'][0]['description']),
            "icon5": str(list_of_data['list'][5]['weather'][0]['icon']),
            "humidity5": str(list_of_data['list'][5]['main']['humidity']),
            "temp5": str(list_of_data['list'][5]['main']['temp']) +'°'+  "C",
            "date5": str(list_of_data['list'][5]['dt_txt']),

            "weather6": str(list_of_data['list'][6]['weather'][0]['description']),
            "icon6": str(list_of_data['list'][6]['weather'][0]['icon']),
            "humidity6": str(list_of_data['list'][6]['main']['humidity']),
            "temp6": str(list_of_data['list'][6]['main']['temp']) + '°'+ "C",
            "date6": str(list_of_data['list'][6]['dt_txt']),

            "weather7": str(list_of_data['list'][7]['weather'][0]['description']),
            "icon7": str(list_of_data['list'][7]['weather'][0]['icon']),
            "humidity7": str(list_of_data['list'][7]['main']['humidity']),
            "temp7": str(list_of_data['list'][7]['main']['temp']) + '°'+ "C",
            "date7": str(list_of_data['list'][7]['dt_txt']),

            "weather8": str(list_of_data['list'][8]['weather'][0]['description']),
            "icon8": str(list_of_data['list'][8]['weather'][0]['icon']),
            "humidity8": str(list_of_data['list'][8]['main']['humidity']),
            "temp8": str(list_of_data['list'][8]['main']['temp']) + '°'+ "C",
            "date8": str(list_of_data['list'][8]['dt_txt']),

            "weather9": str(list_of_data['list'][9]['weather'][0]['description']),
            "icon9": str(list_of_data['list'][9]['weather'][0]['icon']),
            "humidity9": str(list_of_data['list'][9]['main']['humidity']),
            "temp9": str(list_of_data['list'][9]['main']['temp']) + '°'+ "C",
            "date9": str(list_of_data['list'][9]['dt_txt']),

            "weather10": str(list_of_data['list'][10]['weather'][0]['description']),
            "icon10": str(list_of_data['list'][10]['weather'][0]['icon']),
            "humidity10": str(list_of_data['list'][10]['main']['humidity']),
            "temp10": str(list_of_data['list'][10]['main']['temp']) + '°'+ "C",
            "date10": str(list_of_data['list'][10]['dt_txt']),

            "weather11": str(list_of_data['list'][11]['weather'][0]['description']),
            "icon11": str(list_of_data['list'][11]['weather'][0]['icon']),
            "humidity11": str(list_of_data['list'][11]['main']['humidity']),
            "temp11": str(list_of_data['list'][11]['main']['temp']) +'°'+  "C",
            "date11": str(list_of_data['list'][11]['dt_txt']),

            "weather12": str(list_of_data['list'][12]['weather'][0]['description']),
            "icon12": str(list_of_data['list'][12]['weather'][0]['icon']),
            "humidity12": str(list_of_data['list'][12]['main']['humidity']),
            "temp12": str(list_of_data['list'][12]['main']['temp']) +'°'+  "C",
            "date12": str(list_of_data['list'][12]['dt_txt']),

            "weather13": str(list_of_data['list'][13]['weather'][0]['description']),
            "icon13": str(list_of_data['list'][13]['weather'][0]['icon']),
            "humidity13": str(list_of_data['list'][13]['main']['humidity']),
            "temp13": str(list_of_data['list'][13]['main']['temp']) +'°'+  "C",
            "date13": str(list_of_data['list'][13]['dt_txt']),

            "weather14": str(list_of_data['list'][14]['weather'][0]['description']),
            "icon14": str(list_of_data['list'][14]['weather'][0]['icon']),
            "humidity14": str(list_of_data['list'][14]['main']['humidity']),
            "temp14": str(list_of_data['list'][14]['main']['temp']) +'°'+  "C",
            "date14": str(list_of_data['list'][14]['dt_txt']),

            "weather15": str(list_of_data['list'][15]['weather'][0]['description']),
            "icon15": str(list_of_data['list'][15]['weather'][0]['icon']),
            "humidity15": str(list_of_data['list'][15]['main']['humidity']),
            "temp15": str(list_of_data['list'][15]['main']['temp']) +'°'+  "C",
            "date15": str(list_of_data['list'][15]['dt_txt']),

            "weather16": str(list_of_data['list'][16]['weather'][0]['description']),
            "icon16": str(list_of_data['list'][16]['weather'][0]['icon']),
            "humidity16": str(list_of_data['list'][16]['main']['humidity']),
            "temp16": str(list_of_data['list'][16]['main']['temp']) +'°'+  "C",
            "date16": str(list_of_data['list'][16]['dt_txt']),

            "weather17": str(list_of_data['list'][17]['weather'][0]['description']),
            "icon17": str(list_of_data['list'][17]['weather'][0]['icon']),
            "humidity17": str(list_of_data['list'][17]['main']['humidity']),
            "temp17": str(list_of_data['list'][17]['main']['temp']) + '°'+ "C",
            "date17": str(list_of_data['list'][17]['dt_txt']),

            "weather18": str(list_of_data['list'][18]['weather'][0]['description']),
            "icon18": str(list_of_data['list'][18]['weather'][0]['icon']),
            "humidity18": str(list_of_data['list'][18]['main']['humidity']),
            "temp18": str(list_of_data['list'][18]['main']['temp']) + '°'+ "C",
            "date18": str(list_of_data['list'][18]['dt_txt']),

            "weather19": str(list_of_data['list'][19]['weather'][0]['description']),
            "icon19": str(list_of_data['list'][19]['weather'][0]['icon']),
            "humidity19": str(list_of_data['list'][19]['main']['humidity']),
            "temp19": str(list_of_data['list'][19]['main']['temp']) +'°'+ "C",
            "date19": str(list_of_data['list'][19]['dt_txt']),

            "weather20": str(list_of_data['list'][20]['weather'][0]['description']),
            "icon20": str(list_of_data['list'][20]['weather'][0]['icon']),
            "humidity20": str(list_of_data['list'][20]['main']['humidity']),
            "temp20": str(list_of_data['list'][20]['main']['temp']) +'°'+  "C",
            "date20": str(list_of_data['list'][20]['dt_txt']),

            "weather21": str(list_of_data['list'][21]['weather'][0]['description']),
            "icon21": str(list_of_data['list'][21]['weather'][0]['icon']),
            "humidity21": str(list_of_data['list'][21]['main']['humidity']),
            "temp21": str(list_of_data['list'][21]['main']['temp']) +'°'+  "C",
            "date21": str(list_of_data['list'][21]['dt_txt']),

            "weather22": str(list_of_data['list'][22]['weather'][0]['description']),
            "icon22": str(list_of_data['list'][22]['weather'][0]['icon']),
            "humidity22": str(list_of_data['list'][22]['main']['humidity']),
            "temp22": str(list_of_data['list'][22]['main']['temp']) + '°'+ "C",
            "date22": str(list_of_data['list'][22]['dt_txt']),

            "weather23": str(list_of_data['list'][23]['weather'][0]['description']),
            "icon23": str(list_of_data['list'][23]['weather'][0]['icon']),
            "humidity23": str(list_of_data['list'][23]['main']['humidity']),
            "temp23": str(list_of_data['list'][23]['main']['temp']) + '°'+ "C",
            "date23": str(list_of_data['list'][23]['dt_txt']),

            "weather24": str(list_of_data['list'][24]['weather'][0]['description']),
            "icon24": str(list_of_data['list'][24]['weather'][0]['icon']),
            "humidity24": str(list_of_data['list'][24]['main']['humidity']),
            "temp24": str(list_of_data['list'][24]['main']['temp']) + "C",
            "date24": str(list_of_data['list'][24]['dt_txt']),

            "weather25": str(list_of_data['list'][25]['weather'][0]['description']),
            "icon25": str(list_of_data['list'][25]['weather'][0]['icon']),
            "humidity25": str(list_of_data['list'][25]['main']['humidity']),
            "temp25": str(list_of_data['list'][25]['main']['temp']) +'°'+  "C",
            "date25": str(list_of_data['list'][25]['dt_txt']),

            "weather26": str(list_of_data['list'][26]['weather'][0]['description']),
            "icon26": str(list_of_data['list'][26]['weather'][0]['icon']),
            "humidity26": str(list_of_data['list'][26]['main']['humidity']),
            "temp26": str(list_of_data['list'][26]['main']['temp']) +'°'+  "C",
            "date26": str(list_of_data['list'][26]['dt_txt']),

            "weather27": str(list_of_data['list'][27]['weather'][0]['description']),
            "icon27": str(list_of_data['list'][27]['weather'][0]['icon']),
            "humidity27": str(list_of_data['list'][27]['main']['humidity']),
            "temp27": str(list_of_data['list'][27]['main']['temp']) + '°'+ "C",
            "date27": str(list_of_data['list'][27]['dt_txt']),

            "weather28": str(list_of_data['list'][28]['weather'][0]['description']),
            "icon28": str(list_of_data['list'][28]['weather'][0]['icon']),
            "humidity28": str(list_of_data['list'][28]['main']['humidity']),
            "temp28": str(list_of_data['list'][28]['main']['temp']) +'°'+  "C",
            "date28": str(list_of_data['list'][28]['dt_txt']),

            "weather29": str(list_of_data['list'][29]['weather'][0]['description']),
            "icon29": str(list_of_data['list'][29]['weather'][0]['icon']),
            "humidity29": str(list_of_data['list'][29]['main']['humidity']),
            "temp29": str(list_of_data['list'][29]['main']['temp']) + '°'+ "C",
            "date29": str(list_of_data['list'][29]['dt_txt']),

            "weather30": str(list_of_data['list'][30]['weather'][0]['description']),
            "icon30": str(list_of_data['list'][30]['weather'][0]['icon']),
            "humidity30": str(list_of_data['list'][30]['main']['humidity']),
            "temp30": str(list_of_data['list'][30]['main']['temp']) +'°'+  "C",
            "date30": str(list_of_data['list'][30]['dt_txt']),

            "weather31": str(list_of_data['list'][31]['weather'][0]['description']),
            "icon31": str(list_of_data['list'][31]['weather'][0]['icon']),
            "humidity31": str(list_of_data['list'][31]['main']['humidity']),
            "temp31": str(list_of_data['list'][31]['main']['temp']) + '°'+ "C",
            "date31": str(list_of_data['list'][31]['dt_txt']),

            "weather32": str(list_of_data['list'][32]['weather'][0]['description']),
            "icon32": str(list_of_data['list'][32]['weather'][0]['icon']),
            "humidity32": str(list_of_data['list'][32]['main']['humidity']),
            "temp32": str(list_of_data['list'][32]['main']['temp']) + '°'+ "C",
            "date32": str(list_of_data['list'][32]['dt_txt']),

            "weather33": str(list_of_data['list'][33]['weather'][0]['description']),
            "icon33": str(list_of_data['list'][33]['weather'][0]['icon']),
            "humidity33": str(list_of_data['list'][33]['main']['humidity']),
            "temp33": str(list_of_data['list'][33]['main']['temp']) + '°'+ "C",
            "date33": str(list_of_data['list'][33]['dt_txt']),

            "weather34": str(list_of_data['list'][34]['weather'][0]['description']),
            "icon34": str(list_of_data['list'][34]['weather'][0]['icon']),
            "humidity34": str(list_of_data['list'][34]['main']['humidity']),
            "temp34": str(list_of_data['list'][34]['main']['temp']) + '°'+ "C",
            "date34": str(list_of_data['list'][34]['dt_txt']),

            "weather35": str(list_of_data['list'][35]['weather'][0]['description']),
            "icon35": str(list_of_data['list'][35]['weather'][0]['icon']),
            "humidity35": str(list_of_data['list'][35]['main']['humidity']),
            "temp35": str(list_of_data['list'][35]['main']['temp']) + '°'+ "C",
            "date35": str(list_of_data['list'][35]['dt_txt']),

            "weather36": str(list_of_data['list'][36]['weather'][0]['description']),
            "icon36": str(list_of_data['list'][36]['weather'][0]['icon']),
            "humidity36": str(list_of_data['list'][36]['main']['humidity']),
            "temp36": str(list_of_data['list'][36]['main']['temp']) + '°'+ "C",
            "date36": str(list_of_data['list'][36]['dt_txt']),

            "weather37": str(list_of_data['list'][37]['weather'][0]['description']),
            "icon37": str(list_of_data['list'][37]['weather'][0]['icon']),
            "humidity37": str(list_of_data['list'][37]['main']['humidity']),
            "temp37": str(list_of_data['list'][37]['main']['temp']) + '°'+ "C",
            "date37": str(list_of_data['list'][37]['dt_txt']),

            "weather38": str(list_of_data['list'][38]['weather'][0]['description']),
            "icon38": str(list_of_data['list'][38]['weather'][0]['icon']),
            "humidity38": str(list_of_data['list'][38]['main']['humidity']),
            "temp38": str(list_of_data['list'][38]['main']['temp']) + '°'+ "C",
            "date38": str(list_of_data['list'][38]['dt_txt']),

            "weather39": str(list_of_data['list'][39]['weather'][0]['description']),
            "icon39": str(list_of_data['list'][39]['weather'][0]['icon']),
            "humidity39": str(list_of_data['list'][39]['main']['humidity']),
            "temp39": str(list_of_data['list'][39]['main']['temp']) + '°'+ "C",
            "date39": str(list_of_data['list'][39]['dt_txt']),



        }
        print(data)
       #print(we)

    else:
        data = {}

    now=datetime.datetime.now()
    return render(request, "generator/current.html",data)


# Create your views here.
