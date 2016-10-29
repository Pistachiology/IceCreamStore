from django.shortcuts import render
from django.shortcuts import render_to_response, redirect, get_object_or_404, HttpResponseRedirect
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie
from models import User
from django.db import connection
#from .models import *

# Create your views here.
class index(View):
    template_name = "store/index.html"
    def get(self, request):
        #obj, created = User.objects.get_or_create(username="admin", password="1234", isAdmin=True)
        #print created
        return render(request, self.template_name, {})

class register(View):
    template_name = "store/register.html"
    err_message = ""
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        err_occur = "The following errors occur:"
        err_message = ""
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        repassword = request.POST.get('repassword', '')
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        address = request.POST.get('address', '')
        tel = request.POST.get('tel', '')
        company = request.POST.get('company', '')
        if User.objects.filter(username=username).exists():
            err_message += "<li>Username already exists</li>"
        if password != repassword:
            err_message += "<li>Password not match.</li>"
        if firstname == "":
            err_message += "<li>Null value at First Name</li>"
        if lastname == "":
            err_message += "<li>Null value at Last Name</li>"
        if address == "":
            err_message += "<li>Null value at Address</li>"
        if tel == "":
            err_message += "<li>Null value at Tel.</li>"
        if err_message == "":
            newUser = User(username=username, password=password, isAdmin=0, firstName=firstname, lastName=lastname, address=address, tel=tel, company=company)
            newUser.save()
            return render(request, self.template_name)
        else:
            return render(request, self.template_name, {'err_occur': err_occur, 'err_message': err_message})

class all_product(View):
    template_name = "store/all_product.html"

    def get(self, request):
        pass

    def post(self, request):
        pass

class product(View):
    template_name = "store/product.html"

    def get(self, request, product_id):
        pass

    def post(self, request, product_id):
        pass

class history(View):
    template_name = "store/history.html"

    def get(self, request):
        pass

class all_track(View):
    template_name = "store/all_track.html"

    def get(self, request):
        pass

class track(View):
    template_name = "store/track.html"

    def get(self, request, track_id):
        pass

class profile(View):
    template_name = "store/profile.html"

    def get(self, request):
        pass

    def post(self, request):
        pass

class contact_us(View):
    template_name = "store/contact_us.html"

    def get(self, request):
        pass
