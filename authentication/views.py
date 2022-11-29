from django.shortcuts import render
from .models import*
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')



def signup(request):
    if request.method== "POST":
        data = request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        username = data['username']
        password = data['password']
        phone_number = data['phone_number']
        role = data['role']
        print(request.POST)
        users = User.objects.filter(password=password)
        if len(users) > 0:
            return render(request, 'signup.html', {'error': f'{users} already exist'})
        else:
            user = User.objects.create(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.save()
            retr_user = User.objects.filter(username=username)
            # print(f"retrieved_user------> {retr_user.values()}")
            all_details = User.objects.all().values()
            print(f"These are all details---->{all_details}")
            retr_val = retr_user.values()
            id = retr_val[0]["id"]
            # print(f"this is id---->{id}")
            profile = Profile.objects.create(user_id=id, phone_number=phone_number, role=role)
            profile.save()
            return render(request, 'home.html', {"message":f' {username} successfully signed up'})
    return render(request, 'signup.html')



def signin(request):
    if request.method=="POST": 
        data = request.POST
        username = data["username"]
        password = data["password"]
        users = User.objects.filter(username=username)
        if len(users) > 0:
            first_user = users.first()
            if first_user.password==password:
                request.session["username"]= username
                details = User.objects.filter(username=username).values()
                if details:
                    return render(request, 'homepage.html', {"details":details})
                return render(request, 'homepage.html')
            else:
                return render(request, 'signin.html', {'display': 'wrong password'})
        else:
            return render(request, 'signin.html', {'message': 'user does not exist'})
    return render(request, 'signin.html')


