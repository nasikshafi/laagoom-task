
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from authentication import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('users/', views.getuser),
    path('addfavorites/', views.addfavorite),
    path('listfavorites/', views.listfavorite),
    path('creategroup/', views.creategroup),
    path('listgroups/', views.listgroups),

]
