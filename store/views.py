from django.shortcuts import render
from django.shortcuts import render_to_response, redirect, get_object_or_404, HttpResponseRedirect
from django.views import View
from .models import *

# Create your views here.
class index(View):
    template_name = "store/index.html"
    def get(self, request):
        # obj, created = User.objects.get_or_create(username="admin", password="1234", isAdmin=True)
        return render(request, self.template_name, {})


class register(View):
    template_name = "store/register.html"
    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        pass

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


class login(View):
    template_name = "store/login.html"

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        return render(request, self.template_name, {})
        
