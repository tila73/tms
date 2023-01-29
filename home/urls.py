from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    # Home views urls
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),

    #Book views urls
    path('task/', views.task, name="task"),
    path('add', views.addtask, name="addtask"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)