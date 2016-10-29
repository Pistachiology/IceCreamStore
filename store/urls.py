from django.conf.urls import url
#from django.contrib import admin
from . import views

urlpatterns = [
        url(r'^$', views.index.as_view(), name='index'),
        url(r'^register/?$', views.register.as_view(), name='register'),
        url(r'^product/?$', views.all_product.as_view(), name='all_product'),
        url(r'^product/(?P<product_id>[0-9]+)/?$', views.product.as_view(), name='product'),
        url(r'^history/?$', views.history.as_view(), name='history'),
        url(r'^track/?$', views.all_track.as_view(), name='all_track'),
        url(r'^track/(?P<track_id>[0-9]+)/?$', views.track.as_view(), name='track'),
        url(r'^profile/?$', views.profile.as_view(), name='profile'),
        url(r'^contact_us/?$', views.contact_us.as_view(), name='contact_us'),
        # TODO: fix url redirection
        url(r'^login/?$', views.login.as_view(), name='login'),
        url(r'^.*$', views.index.as_view(), name='somethingelse'),
        
]
