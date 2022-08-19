from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analize(request):
    #get the text
    textdj=request.GET.get('text','default')
    removepunk=request.GET.get('removepunk','default')
    capitalize=request.GET.get('cap','default')
    fcapitalize=request.GET.get('fcap','default')
    newl=request.GET.get('newline','off')
    extsp=request.GET.get('extrasp','off')
    analized=""
    
    if removepunk=='on':
        punc='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for char in textdj:
            if char not in punc:
                analized=analized+char
        params={'purpose':'Remove punctuatioation','analize_text':analized}
    if capitalize=='on':
        analized=textdj.capitalize()
        params={'purpose':'Capitalize first latter','analize_text':analized}
    if fcapitalize=='on':
        for char in textdj:
            analized=analized+char.upper()
        params={'purpose':'Upper case all','analize_text':analized}
    if newl=='on':
        for char in textdj:
            if char !='\n':
                analized=analized+char
        params={'purpose':'remove new line','analize_text':analized}
    if extsp=='on':
        analized=""
        for index,char in enumerate(textdj):
            if textdj[index]==" " and textdj[index+1]==" ":
                pass
            else:
                analized=analized+char
        params={'purpose':'Extra space removbbe','analize_text':analized}
    if removepunk == 'on' and capitalize == 'on':
        for char in textdj:
            if char not in punc:
                analized = analized+char
        analize.capitalize()

        params = {'purpose': 'Remove Punctuatioation First Letter Capitalise',
            'analize_text': analized}
        if fcapitalize=='on':
            analized.upper()
            params = {'purpose': 'Remove Punctuatioation, First Letter Capitalise, All Upper Case',
            'analize_text': analized}
        if newl=='on':
            for char in analized:
                if char !='\n':
                    analized=""+char
            params={'purpose':'remove new line','analize_text':analized}

    if removepunk == 'on' and capitalize == 'on':
        for char in textdj:
            if char not in punc:
                analized = analized+char
        analize.capitalize()

        params = {'purpose': 'Remove Punctuatioation First Letter Capitalise',
            'analize_text': analized}

    return render(request,'analize.html',params)
