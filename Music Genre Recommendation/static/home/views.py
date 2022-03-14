from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
info = {}


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is homepage")


def choose_singer(request):
    # return HttpResponse("This is choose_singer")
    return render(request, 'choose_singer.html')


def choose_singer2(request):
    # return HttpResponse("This is choose_singer")
    return render(request, 'choose_singer2.html')


def choose_singer3(request):
    # return HttpResponse("This is choose_singer")
    return render(request, 'choose_singer3.html')

# def input_hindi_(request):
#     return render(request, 'input_hindi_.html')


def emotion_detect(request):
    # return HttpResponse("This is emotion_detect")
    
    return render(request, 'emotion_detect.html')


def input_hindi_1(request):
    return render(request, 'input_hindi_1.html')


def input_hindi_2(request):
    return render(request, 'input_hindi_2.html')


def input_hindi_3(request):
    return render(request, 'input_hindi_3.html')


def input_hindi_4(request):
    return render(request, 'input_hindi_4.html')


def input_english_1(request):
    return render(request, 'input_english_1.html')


def input_english_2(request):
    return render(request, 'input_english_2.html')


def input_english_3(request):
    return render(request, 'input_english_3.html')


def input_english_4(request):
    return render(request, 'input_english_4.html')

def emotion_detect(request):
    # return HttpResponse("This is emotion_detect")
    
    return render(request, 'emotion_detect.html')
    
def regional_input(request):
    title = request.POST.get('quantity')
    context = {}
    print(title)
    return render(request, "input_regional.html", context)
