from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from asgiref.sync import sync_to_async

from signin import hub

async def login_view(request):
    if request.method == "GET":
        print('desoues de get')
        return render(request, 'signin/login.html')
    
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = await sync_to_async(authenticate)(request, username=username, password=password)
        print('despues de else')
        if user is not None:
            await sync_to_async(login)(request, user)
            return render(request, 'signin/home.html')
        else:
            return HttpResponse("Invalid username or password.")

async def home():
    results = await hub.main('', '')
    data = {'results': results}  
    return JsonResponse(data)
