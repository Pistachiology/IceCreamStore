from django.shortcuts import render
from django.shortcuts import render_to_response, redirect, get_object_or_404, HttpResponseRedirect
from django.views import View
from .models import *

# Create your views here.
class index(View):
        template_name = "store/index.html"
        def get(self, request):
            #obj, created = User.objects.get_or_create(username="admin", password="1234", isAdmin=True)
            #print created
            return render(request, self.template_name, {})

