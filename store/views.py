from django.shortcuts import render
from django.shortcuts import render_to_response, redirect, get_object_or_404, HttpResponseRedirect
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie
from django.db import connection
from .models import *

# Create your views here.
class index(View):
    template_name = "store/index.html"
    def get(self, request):
        #obj, created = User.objects.get_or_create(username="admin", password="1234", isAdmin=True)
        #print created
        return render(request, self.template_name, {})

class login(View):
    template_name = "store/login.html"

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        if request.POST['password'] == request.POST['repassword']:
            pass
        else:
            return render(request, self.template_name, {})
        return render(request, self.template_name, {})

class register(View):
    template_name = "store/register.html"
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        response = {}
        response['err_occur'] = "The following errors occur:"
        response['err_message'] = ''
        for key in request.POST.keys():
            response[key] = request.POST.get(key, '')
        if User.objects.filter(username=response['username']).exists():
            response['err_message'] += "<li>Username already exists</li>"
        if response['username'] == "":
            response['err_message'] += "<li>Username is required</li>"
        if response['password'] != response['repassword']:
            response['err_message'] += "<li>Password not match.</li>"
        if response['password'] == "":
            response['err_message'] += "<li>Password is required</li>"
        if response['first_name'] == "":
            response['err_message'] += "<li>Null value at First Name</li>"
        if response['last_name'] == "":
            response['err_message'] += "<li>Null value at Last Name</li>"
        if response['address'] == "":
            response['err_message'] += "<li>Null value at Address</li>"
        if response['tel'] == "":
            response['err_message'] += "<li>Null value at Tel.</li>"
        if response['err_message'] == "":
            newUser = User(username=response['username'],
                           password=response['password'],
                           is_admin=0,
                           first_name=response['first_name'],
                           last_name=response['last_name'],
                           address=response['address'],
                           tel=response['tel'],
                           company=response['company'])
            newUser.save()
            return render(request, self.template_name)
        else:
            return render(request, self.template_name, response)

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
