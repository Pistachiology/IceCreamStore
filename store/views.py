from django.shortcuts import render
from django.shortcuts import render_to_response, redirect, get_object_or_404, HttpResponseRedirect
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import *

# Create your views here.
class index(View):
    template_name = "store/index.html"
    def get(self, request):
        #obj, created = User.objects.get_or_create(username="admin", password="1234", isAdmin=True)
        #print created
        return render(request, self.template_name, {})

class login_view(View):
    template_name = "store/login.html"

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        err_message = "KUY"
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, self.template_name, {'err_message': user})
        else:
            return render(request, self.template_name, {'err_message': err_message})

class register(View):
    template_name = "store/register.html"

    @method_decorator(login_required)
    def get(self, request):
        #if not 'is_logged_in' in request.session or not request.session['is_logged_in']:
        #    return redirect("/store/login")
        return render(request, self.template_name)

    def post(self, request):
        response = {}
        response['err_occur'] = "The following errors occur:"
        response['err_message'] = ""
        for key in request.POST.keys():
            response[key] = request.POST.get(key, '')
        if CustomUser.objects.filter(username=response['username']).exists():
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
            newUser = CustomUser(username=response['username'],
                           is_superuser=0,
                           first_name=response['first_name'],
                           last_name=response['last_name'],
                           address=response['address'],
                           tel=response['tel'],
                           company=response['company'])
            newUser.set_password(response['password'])
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
