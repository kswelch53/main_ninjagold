from django.shortcuts import render, HttpResponse, redirect
from random import randint

# Create your views here.
def index(request):
    if 'goldcounter' not in request.session:
        request.session['goldcounter'] = 0
        request.session['updatelist'] = list()
    return render(request, 'myapp/index.html')

def clear(request):
    request.session['goldcounter'] = 0
    request.session['updatelist'] = list()
    return redirect('/')

def processmoney(request):
    winlose = "earned"
    if request.POST["place"] == "farm":
        gold = randint(10,20)
        updatelist = winlose, gold, "farm"
        request.session['goldcounter'] = request.session['goldcounter'] + gold
    if request.POST["place"] == "cave":
        gold = randint(5,10)
        updatelist = winlose, gold, "cave"
        request.session['goldcounter'] = request.session['goldcounter'] + gold
    if request.POST["place"] == "house":
        gold = randint(2,5)
        updatelist = winlose, gold, "house"
        request.session['goldcounter'] = request.session['goldcounter'] + gold
    if request.POST["place"] == "casino":
        gold = randint(-50, 50)
        if gold >= 0:
            updatelist = winlose, gold, "casino"
            request.session['goldcounter'] = request.session['goldcounter'] + gold
        else:
            gold = abs(gold)
            winlose = "lost"
            updatelist = winlose, gold, "casino"
            request.session['goldcounter'] = request.session['goldcounter'] + gold
    request.session['updatelist'].append(updatelist)
    return redirect('/')
