from django.shortcuts import render

# Create your views here.
def index(request):
    string = "helloWorld"
    return render(request,'home.html',{'string':string})
def languageList(request):
	language_list = ['C','C++','Java','python']
	return render(request,'languageList.html',{'language_list':language_list})
def sequences(request):
	List = map(str,range(100))
	return render(request,'sequences.html',{'list':List})
