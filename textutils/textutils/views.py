# I have created this file - Sujal
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    global params
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    ExtraSpaceRemover = request.POST.get('ExtraSpaceRemover', 'off')
    NewLineRemover = request.POST.get('NewLineRemover', 'off')

    if removepunc == "on":
        punctuations = '''!()-{}[];:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if ExtraSpaceRemover == "on":
        analyzed = ""
        prev_char = ""
        for char in djtext:
            if not (prev_char == " " and char == " "):
                analyzed += char
            prev_char = char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed

    if NewLineRemover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}

    if removepunc != "on" and fullcaps != "on" and NewLineRemover != "on" and ExtraSpaceRemover != "on":
        return HttpResponse("Please select any operation and try again")

    return render(request, 'analyze.html', params)

def contact_us(request):
    return render(request, 'contact_us.html')


def about_us(request):
    return render(request, 'about_us.html')
