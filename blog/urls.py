from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from blog.views import feed,profile,register,proyecto,index
 
urlpatterns = [
	path('', index, name='index'),
	path('feed/', feed.as_view(), name='feed'),
	path('profile/', profile, name='profile'),
	path('profile/<str:username>/', profile, name='profile'), #esta es user y proyecto
	path('register/', register, name='register'),
	path('login/', LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='index.html'), name='logout'),
	path('proyecto/', proyecto, name='proyecto'),
	
	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



