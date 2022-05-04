from unicodedata import name
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('player',views.player,name='player'),
    path('trainer',views.trainer,name='trainer'),
    path('fee',views.fee,name='fee'),
    path('contact',views.contact,name='contact')
    

]
