from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from blog.views import feed,profile,register,proyecto
 
urlpatterns = [
	path('', feed.as_view(), name='feed'),
	path('profile/', profile, name='profile'),
	path('profile/<str:username>/', profile, name='profile'), #esta es
	path('register/', register, name='register'),
	path('login/', LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
	path('proyecto/', proyecto, name='proyecto'),
	# path('follow/<str:username>/', follow, name='follow'),
	# path('unfollow/<str:username>/', unfollow, name='unfollow'),
	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# urlpatterns = [
#     path("", home_view, name="home"),
# #    path("profile/", profile, name="profile"),
# #    path("register/" ,register, name="register"),
#     ]