from django.shortcuts import render
from .models import*
from . forms import Studentsforms

# Create your views here.

def student(request):
    return render(request, 'students_page.html')


def new_student(request):
    if request.method=="POST":
        data = request.POST
        first_name = data['first_name']
        middle_name = data['middle_name']
        last_name = data['last_name']
        date_of_birth = data['date_of_birth']
        age = data['age']
        address = data['address']
        course = data['course']
        new_student = Studentprofile.objects.create(first_name=first_name, middle_name=middle_name, last_name=last_name, date_of_birth=date_of_birth, age=age, address=address, course=course)
        new_student.save()
        all_students = Studentprofile.objects.all()
        context = {"all_students":all_students}
        return render(request, 'students_page.html', context)
    return render(request, 'add_students.html')


def update_student(request,pk):
        data = request.POST
        update = Studentprofile.objects.get(id=pk)
        update_form = Studentsforms( instance=update)
        if request.method=="POST":
            update_form = Studentsforms(data, instance=update)
            if update_form.is_valid():
                update_form.save()
                all_students = Studentprofile.objects.all()
                context = {"all_students":all_students}
            return render(request, 'students_page.html', context)
        return render(request, 'update_form.html', {"update":update, "update_form":update_form})


def delete_stud(request,pk):
    delete_student = Studentprofile.objects.get(id=pk)
    delete_student.delete()
    all_students = Studentprofile.objects.all()
    context = {"all_students":all_students}
    return render(request, 'students_page.html', context)


    