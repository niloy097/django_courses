from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    d = {"prices" : [5, 10, 15],"name" : "niloy", "text" : "T m re c", "val" : 11,
         "names" : ['xavier', 'yellobowl', 'zixer'], 'slashVal' : "Niloy'Anaya", "Todays_Date" : datetime.datetime.now(),
         "sortItem" : [
                        {'name': 'zed', 'age': 19},
                        {'name': 'amy', 'age': 22},
                        {'name': 'joe', 'age': 31},
                    ],
         "obj" : [{
                    'id' : 1,
                    'name' : 'Gay Luna',
                    'country' : 'Spain, Bercelona',
                    'stadium' : 'Camp Nue'
                },
                {
                    'id' : 2,
                    'name' : 'Real Madrid',
                    'country' : 'Spain, Madrid',
                    'stadium' : 'Santiago Bernabeu' 
                },
                {
                    'id' : 3,
                    'name' : 'Manchester United',
                    'country' : 'England, Manchester',
                    'stadium' : 'Old Trafford'
                }]
         }
    # context must be a dictionary
    return render(request, 'index.html', context=d) 
