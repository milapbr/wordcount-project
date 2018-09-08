from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):

    #return HttpResponse('Hello')
    #return render(request, 'home.html', {'hithere':'this is me'})
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def viewsfile(request):
    return render(request, 'viewsfile.html')

def homesfile(request):
    return render(request, 'homesfile.html')

def counts(request):
    fulltext=request.GET['fulltext']
    #print (fulltext)
    wordlist=fulltext.split()
    wordcountdictionary={}
    for word in wordlist:
        if word in wordcountdictionary:
            wordcountdictionary[word]+=1
        else:
            wordcountdictionary[word]=1
    
    sortedw= sorted(wordcountdictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'wordcountdictionary': sortedw})
  