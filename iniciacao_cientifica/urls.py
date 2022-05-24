from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('user', views.user, name='user'),
    path('user/<int:id>/', views.deleteUser, name='deleteUser'),
    path('accounts/login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('article', views.article, name='article'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

