from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import comment,search_results,login,logout,profile,follow,unfollow

urlpatterns=[
    url('^$', views.index, name = 'index'),
    url('new/image/', views.upload_image, name = 'new-image'),
    url('register/', views.registerPage, name = 'register'),
    url('login/', views.loginPage, name = 'login'),
    url('logout/', views.logoutUser, name = 'logout'),
    url('profile/',views.profile, name= 'profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url('comments/<int:id>', comment, name ='comments'),
    url('follow/<pk>', follow, name ='follow'),
    url('unfollow/<pk>', unfollow, name = 'unfollow'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
