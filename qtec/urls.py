
from django.contrib import admin
from django.urls import path, include
from users.views import Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('searchhistory.urls')),

]
