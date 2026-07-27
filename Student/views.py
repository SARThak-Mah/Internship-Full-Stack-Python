from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from .models import Student

# Create your views here.

def home(request):
    return render(request, 'MyApp/home.html')

def student_form(request):
    return render(request, 'MyApp/student_form.html')


def student_data(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        course = request.POST.get('course')
        city = request.POST.get('city')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        about = request.POST.get('about')

        skills_list = request.POST.getlist('skills')
        skills = ", ".join(skills_list)

        photo = request.FILES.get('profile_photo')

        if photo:
            ext = photo.name.split('.')[-1].lower()
            if ext not in ['jpg', 'jpeg', 'png']:
                context = {
                    'msg': "Error: Invalid image format! Please upload JPG or PNG files only."
                }
                return render(request, 'MyApp/student_form.html', context)

        student = Student(
            full_name = full_name,
            email = email,
            mobile = mobile,
            course = course,
            city = city,
            gender = gender,
            dob = dob,
            skills = skills,
            profile_photo = photo,
            about = about
        )
        student.save()

        return redirect('/MyApp/show_students/')

    return render(request, 'MyApp/student_form.html')



def show_students(request):
    records = Student.objects.all()
    context = {'students': records}
    return render(request, 'MyApp/show_student.html', context)
