from django.shortcuts import render, redirect
from tourapp.models import TourPlace, AdminModel, RegisterModel, LoginModel
from django.db.models import Q
from django.views.generic import TemplateView, DetailView, View, CreateView
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def admins(request):
    return render(request, "admin.html")

def admin_login(request):
    username = request.POST.get("a1")
    password = request.POST.get("a2")
    try:
        AdminModel.objects.get(Username=username, Password=password)
        return render(request, "admin-home.html")
    except AdminModel.DoesNotExist:
        return render(request, "admin.html", {"error": "Invalid Details"})

def about(request):
    return render(request, "about.html")

def register(request):
    return render(request, "register.html")

def searchbar(request):
    place = TourPlace.objects.all()
    if request.method == "POST":
        search = request.POST.get("searchs")
        results = TourPlace.objects.filter(Q(Place__icontains=search))
        return render(request, "searchbar.html", {"result": results, "place": place})


class details(DetailView):
    template_name = "Detail.html"
    model = TourPlace

def Admin_Details(request):
    place = request.POST.get("p1")
    slug = request.POST.get("p2")
    inside_place = request.POST.get("p3")
    persons = request.POST.get("p4")
    image = request.FILES["p5"]
    details = request.POST.get("p6")
    marked_price = request.POST.get("p7")
    confirm_price = request.POST.get("p8")
    offer_valid = request.POST.get("p9")
    TourPlace(Place=place, slug=slug, Inside_Places=inside_place, Persons=persons, Image=image, Details=details,
              Marked_Price=marked_price, Confirm_Price=confirm_price, Offer_Valid=offer_valid).save()
    messages.success(request, "Uploaded Successfully")
    return render(request, "admin-home.html")

def register_up(request):
    name = request.POST.get("r1")
    username = request.POST.get("r2")
    email = request.POST.get("r3")
    contact = request.POST.get("r4")
    password1 = request.POST.get("r5")
    password2 = request.POST.get("r6")
    address = request.POST.get("r7")
    secret = request.POST.get("r8")
    match = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    match1 = "abcdefghijklmnopqrstuvwxyz"
    integer = "1234567890"
    spl_chr = "!@#$%^&*"
    for x in password1:
        if x in spl_chr:
            for y in password1:
                if y in match:
                    for z in password1:
                        if z in match1:
                            for a in password1:
                                if a in integer:
                                    if len(str(password1)) > 7 and len(str(password1)) < 17:
                                        if len(str(contact)) == 10:
                                            if password1 == password2:
                                                RegisterModel(Name=name, Username=username, Email=email, Contact=contact, Password1=password1,
                                                              Password2=password2, Address=address, Secret_Info=secret).save()
                                                LoginModel(Username=username, Password=password1).save()
                                                messages.success(request, "Registered Successfully")
                                                return redirect("register")
                                            else:
                                                return render(request, "register.html", {"error6": "Password not Matching"})
                                        else:
                                            return render(request, "register.html", {"error": "Invalid Contact Number"})
                                    else:
                                        return render(request, "register.html", {"error5": "Password should be between 7 and 17 characters"})
                            else:
                                return render(request, "register.html", {"error4": "Choose atleast one Integer"})
                    else:
                        return render(request, "register.html", {"error3": "Choose atleast one Small Alphabet"})
            else:
                return render(request, "register.html", {"error2": "Choose atleast one Caps Alphabet"})
    else:
        return render(request, "register.html", {"error1": "Choose atleast one Special Character from !,@,#,$,%,^,&,*"})

def login(request):
    return render(request, "login.html")

def login_up(request):
    username = request.POST.get("l1")
    password = request.POST.get("l2")
    try:
        LoginModel.objects.get(Username=username, Password=password)
        return render(request, "home.html", {"name": username})
    except LoginModel.DoesNotExist:
        return render(request, "login.html", {"error": "Username and Password Doesn't Match"})