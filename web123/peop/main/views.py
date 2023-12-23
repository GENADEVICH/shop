from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def proddog (request):
    return render(request, 'main/proddog.html')

def gprodcat (request):
    return render(request, 'main/gprodcat.html')

def prodbird (request):
    return render(request, 'main/prodbird.html')

def prodgriz (request):
    return render(request, 'main/prodgriz.html')

def reviews (request):
    return render(request, 'main/reviews.html')

def order (request):
    return render(request, 'main/order.html')
