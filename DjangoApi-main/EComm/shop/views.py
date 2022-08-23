from django.shortcuts import render
import requests
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.


def home(request):

    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        print(request.POST, "-----data")
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        # password=request.POST.get('password')
        print(username, "-----username")

        r = requests.post(
            'http://127.0.0.1:8000/api/createuser', data=request.POST)

        if r.status_code == 201:
            data = r.json()
            print(data)

        messages.success(request, "Sucessfully Created")
        return render(request, 'signup.html')

    return render(request, 'signup.html')


def getuser(request):

    response = requests.get('http://127.0.0.1:8000/api/getuser').json()

    return render(request, 'showuser.html', {'response': response})


def Updateuser(request, id):
    if request.method == "POST":
        print(request, "data-------")

        # print(request.PUT,"Data________")
        response = requests.put(
            f'http://127.0.0.1:8000/api/updateuser/{id}/', data=request.POST)
        return render(request, 'userUpdate.html')

    if request.method == "POST":
        print(request.POST)

    return render(request, 'userUpdate.html', {"id": id})   



def deleteuser(request):
    if request.method == "POST":
        id = request.POST["id"]
        print("id")
        response = requests.delete(
            f'http://127.0.0.1:8000/api/deleteuser/{id}/')

    return redirect('getuser')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is None:
            login1(request, user)
            first_name = user.first_name
            return render(request, "index.html", {'first_name': first_name})

        else:
            messages.error(request, "Not Sucess")
            return redirect('home')

    return render(request, "signin.html")


def signout(request):
    # response=requests.get('http://127.0.0.1:8000/api/login')

    return render(request, "showuser.html")


def CreatePro(request):

    if request.method == "POST":
        # print(request.POST,"Data________")
        response = requests.post(
            'http://127.0.0.1:8000/api/createproduct/', data=request.POST)
        print(response)
        print(request)
        return render(request, 'createpro.html')

    return render(request, 'createpro.html')


def proShow(request):

    response = requests.get('http://127.0.0.1:8000/api/getproduct').json

    return render(request, 'proshow.html', {'response': response})


def UpdatePro(request, id):
    if request.method == "PUT":
        print(request, "data-------")

        # print(request.PUT,"Data________")
        response = requests.put(
            f'http://127.0.0.1:8000/api/updateproduct/{id}/', data=request.PUT)
        return render(request, 'proUpdate.html')

    if request.method == "POST":
        print(request.POST)

    return render(request, 'proUpdate.html', {"id": id})


def DelPro(request):
    if request.method == "POST":
        id = request.POST["id"]
        response = requests.delete(
            f'http://127.0.0.1:8000/api/deleteproduct/{id}/')
        print(response)

    return redirect('proShow')

    # return render(request,'proshow.html')


def CreateCate(request):

    if request.method == "POST":
        print(request.POST, "Data________")
        response = requests.post(
            'http://127.0.0.1:8000/api/createcategory/', data=request.POST)
        print(response)
        return render(request, 'createCate.html')

    return render(request, 'createCate.html')


def showCate(request):

    response = requests.get('http://127.0.0.1:8000/api/getcategory/').json
    return render(request, 'showcate.html', {'response': response})


def updateCate(request, id):
    if request.method == "POST":
        print(request.POST, "data-------")

        response = requests.put(
            f'http://127.0.0.1:8000/api/updatecategory/{id}/', data=request.POST)
        return render(request, 'updateCate.html')

    if request.method == "POST":
        print(request.POST)

    return render(request, 'updateCate.html', {"id": id})


def DelCategory(request):
    if request.method == "POST":
        id = request.POST["id"]
        response = requests.delete(
            f'http://127.0.0.1:8000/api/deleteCategory/{id}/')

    return redirect('showCate')
