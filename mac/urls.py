from unicodedata import name
from xml.etree.ElementInclude import include
from django.urls import path
from . import views


urlpatterns = [
    path('home',views.home,name='home'),
    path('register',views.registration,name='register'),
    path('login',views.loginpage,name='login'),
    path('logout',views.logoutPage,name='logout'),
    path('create/<str:pk>',views.create, name='create'),
    path('delete/<str:pk>',views.deletelink, name='delete'),
    path('deleteli/<str:pk>',views.deleteli, name='deleteli'),
    path('share/<int:id>', views.share , name='share' ),
    path('' ,views.wel , name='welcome'),
    path('how_to_use' ,views.use , name='how_to_use'),
    path('<str:pk>' ,views.crash , name='crash'),
    path('<str:pk>/<str:mk>' ,views.crash , name='crash'),
]