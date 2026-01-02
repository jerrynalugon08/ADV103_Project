from django.shortcuts import render

def home(request):
    # If you want to pass context variables, add them here
    return render(request, "home.html")

def gallery1(request):
    return render(request, 'gallery1.html')

def gallery2(request):
    return render(request, 'gallery2.html')

def gallery3(request):
    return render(request, 'gallery3.html')

def gallery4(request):
    return render(request, 'gallery4.html')

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')



