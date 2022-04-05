from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Create your views here.

def index(request):
    logout(request)
    return render(request,"login.html")

def registration(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        role = request.POST["role"]
        try:
            User.objects.get(username=username)
            messages.info(request,"User with that email already exists.")
            return redirect("/registration")
        except User.DoesNotExist:
            e = User()
            e.username = username
            e.password = make_password(password)
            e.first_name = first_name
            e.last_name = last_name
            e.save()

        a = Profile()
        a.first_name = first_name
        a.last_name = last_name
        a.email = username
        a.role = role
        a.user = e
        a.save()



        messages.info(request, "Registration is succesfully done")
        return redirect("/")
    else:
        return render(request, "registration.html")


def loginFunction(request):
    if request.method == "POST":
        username = request.POST["usr"]
        password = request.POST["pass"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            role = request.user.profile.role
            if role == "student":
                return redirect("/student")
            elif role == "admin":
                return redirect("/adm")
            else:
                messages.info(request, "you are not authorised to view this!")
                return redirect("/")

        else:

            messages.info(request, "User is not there")
            return redirect("/")
    else:
        return redirect("/")

@login_required
def studentDashboard(request):
    role = request.user.profile.role
    if role == "student":
        book = Book.objects.all()
        data ={"book":book}
        return render(request, "studentdashboard.html",data)
    else:
        messages.info(request, "You are not authorised to view this!")
        return redirect("/")


@login_required
def adminDashboard(request):
    role = request.user.profile.role
    if role == "admin":
        if request.method == "POST":
            book_name = request.POST["book_name"]
            published_date = request.POST["published_date"]
            author = request.POST["author"]
            publisher = request.POST["publisher"]
            category = request.POST["category"]
            book_image = request.FILES["book_image"]
            e = Book()
            e.book_name = book_name
            e.published_date = published_date
            e.author = author
            e.publisher = publisher
            e.category = category
            e.book_image = book_image
            e.username = request.user.username
            e.save()
            return redirect("/adm")


        else:
            book = Book.objects.all()
            data = {"book": book}

            return render(request, "admindashboard.html",data)
    else:
        messages.info(request, "You are not authorised to view this!")
        return redirect("/")

@login_required
def updateBook(request,id):
    role = request.user.profile.role
    e = Book.objects.get(id=id)
    if role == "admin":
        if request.method == "POST":
            book_name = request.POST["book_name"]
            published_date = request.POST["published_date"]
            author = request.POST["author"]
            publisher = request.POST["publisher"]
            category = request.POST["category"]
            book_image = request.FILES.get("book_image")

            e.book_name = book_name
            e.published_date = published_date
            e.author = author
            e.publisher = publisher
            e.category = category
            if book_image:
                e.book_image = book_image
            e.save()
            messages.info(request, "Updated Successfully!")
            return redirect("/adm")
        else:
            data = {"book":e}
            return render(request,"updatebook.html",data)

@login_required
def deleteBook(request,id):
    user = request.user.username
    e = Book.objects.get(id=id)
    if user == e.username:
        e.delete()
        messages.info(request, "Book Deleted Successfully!!")
        return redirect("/adm")
    else:
        messages.info(request, "You are not authorised!")
        return redirect("/")
