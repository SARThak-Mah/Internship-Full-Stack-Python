from django.shortcuts import render, redirect
from .models import Employee, Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def home(request):
    Student = {
        "roll_no": 3160,
        "name": "Sarthak",
        "age": "20",
    }
    return render(request, 'myapp/home.html', Student)

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

def empform(request):
    return render(request, 'myapp/empform.html')

def empdata(request):
    btn = request.GET.get('sub')
    if btn == "Submit":
        eid = request.GET.get('eid')
        ename = request.GET.get('ename')
        eloc = request.GET.get('eloc')
        esal = request.GET.get('esal')

        # Instantiate and save instance structure fields to database tracking
        e = Employee(eid=eid, ename=ename, eloc=eloc, esal=esal)
        e.save()

        p = {'msg': "Record Inserted..."}
        return render(request, 'myapp/empform.html', p)
    if btn == "Display":
        record = Employee.objects.all()
        context = {"data": record}
        return render(request, "myapp/empform.html", context)

    return render(request, 'myapp/empform.html')

def crud(request):
    return render(request, 'myapp/crud.html')

def crud_data(request):
    btn = request.GET.get('sub')
    id = request.GET.get('eid')
    context = {}
    if btn == "Display":
        try:
            record = Employee.objects.get(eid=id)
            context = {'data': record}
        except Employee.DoesNotExist:
            context = {'msg': "Record Not Found."}
        return render(request, 'myapp/crud.html', context)

    if btn == "Delete":
        Employee.objects.filter(eid=id).delete()
        context = {'msg': "Record Deleted."}
        return render(request, 'myapp/crud.html', context)

    if btn == "Edit":
        record = Employee.objects.get(eid=id)
        context = {"data": record}
        return render(request, 'myapp/edit.html', context)

    return render(request, 'myapp/crud.html')

def update(request):
    if request.method == "POST":
        # Phase 2: Capture submitted changes and overwrite the database record
        eid = request.POST.get('eid')
        name = request.POST.get('ename')
        location = request.POST.get('eloc')
        salary = request.POST.get('esal')

        # Pull matching primary key record safely
        record = Employee.objects.get(id=eid)

        # Fixed: Updated properties to accurately track your true model schema fields
        record.ename = name
        record.eloc = location
        record.esal = salary
        record.save()
        context = {'msg': "Record Updated.", 'data': record}

        # Return cleanly back to the CRUD interface display log
        return render(request, 'myapp/crud.html', context)

    else:
        # Phase 1: Read incoming GET parameter ID to pre-populate form elements
        eid = request.GET.get('id')
        record = Employee.objects.get(id=eid)
        return render(request, 'myapp/edit.html', {'data': record})

def product(request):
    return render(request,'myapp/product.html')
def product_data(request):
    btn=request.POST.get('sub')
    if btn=="Submit":
        prod=Product()
        prod.pname=request.POST.get('pname')
        prod.pcat=request.POST.get('pcat')
        prod.pprice=request.POST.get('pprice')
        prod.pdate=request.POST.get('pdate')
        if len(request.FILES)!=0:
            prod.pimage=request.FILES['pfile']
        prod.save()
        context={"msg":"File Uploaded Successfully.."}
        return render(request,'myapp/product.html',context)

    if btn=="Display":
        return redirect('show_product')

def show_product(request):
    record = Product.objects.all()
    context = {'data': record}
    return render(request, 'myapp/show_product.html', context)

def delete(request):
    id=request.GET.get("id")
    #print(id)
    Employee.objects.filter(eid=id).delete()

    return render(request, "myapp/empform.html")
def edit(request):
    id = request.GET.get("id")

def signupform(request):
    return render(request,'myapp/signupform.html')
def signupdata(request):
    uname=request.POST.get("uname")
    password=request.POST.get('password')
    email=request.POST.get('email')
    data = User.objects.create_user(uname, email, password)
    data.save()
    return redirect("/myapp/loginform")

def loginform(request):
    return render(request,'myapp/loginform.html')
def logindata(request):
    uname = request.POST.get("uname")
    password = request.POST.get('password')
    user = authenticate(username=uname, password=password)
    if user is not None:
        login(request, user)
        return redirect('/myapp/home')
    else:
        return redirect('/myapp/loginform')

def userlogout(request):
    logout(request)
    return redirect('/myapp/loginform')

