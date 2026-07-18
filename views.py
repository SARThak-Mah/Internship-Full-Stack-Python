from django.shortcuts import render
from .models import Employee


# Example A: Passing a dictionary variable string package to a view
def home(request):
    person = {
        "eid": 1,
        "name": "Sarthak",
        "age": "20",
        "sal": "100000"
    }
    return render(request, 'myapp/home.html', person)

# Example B: Fetching dynamic inputs out of custom request arguments
def getform(request):
    return render(request, 'myapp/myform.html')


def data(request):
    uname = request.GET.get('Uname')
    password = request.GET.get('pass')
    age = request.GET.get('age')

    p = {
        "name": uname,
        "password": password,
        "age": age
    }
    return render(request, 'myapp/myform.html', p)


# Example C: Form data mapping database row saves
def empform(request):
    return render(request, 'myapp/empform.html')


def empdata(request):
    btn = request.GET.get('sub')
    if btn == "submit":
        eid = request.GET.get('eid')
        ename = request.GET.get('ename')
        eloc = request.GET.get('eloc')
        esal = request.GET.get('esal')

        # Instantiate and save instance structure fields to database tracking
        e = Employee(eid=eid, ename=ename, eloc=eloc, esal=esal)
        e.save()

        p = {'msg': "Record Inserted..."}
        return render(request, 'myapp/empform.html', p)

    return render(request, 'myapp/empform.html')

def crud(request):
    return render(request, 'myapp/crud.html')

def crud_data(request):
    btn = request.GET.get('sub')
    id = request.GET.get('eid')
    context = {}
    if btn == "display":
        try:
            record = Employee.objects.get(eid=id)
            context = {'data': record}
        except Employee.DoesNotExist:
            context = {'msg': "Record Not Found."}
        return render(request, 'myapp/crud.html', context)

    elif btn == "delete":
        Employee.objects.filter(eid=id).delete()
        context = {'msg': "Record Deleted."}
        return render(request, 'myapp/crud.html', context)
    return render(request, 'myapp/crud.html')