from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$', views.index, name = 'index'),
    url('new/image/', views.upload_image, name = 'new-image'),
    url('register/', views.registerPage, name = 'register')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
