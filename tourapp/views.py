from django.shortcuts import render, redirect
from tourapp.models import TourPlace, AdminModel
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
    TourPlace(Place=place, slug=slug, Inside_Places=inside_place, Persons=persons, Image=image, Details=details,
              Marked_Price=marked_price, Confirm_Price=confirm_price).save()
    messages.success(request, "Uploaded Successfully")
    return render(request, "admin-home.html")