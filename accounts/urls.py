from django.urls import path
from accounts.views import gan, signup, signin, signout, base

app_name = 'accounts'
urlpatterns = [
    path('',gan,name='gan'),
    path('signup/',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('signout/',signout,name='signout'),
]
