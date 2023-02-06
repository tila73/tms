from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Home views urls
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),

    path('register/', views.register, name="register"),    
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', views.logout_view, name="logout"),

    #Task views urls
    path('task/', views.task, name="task"),
    path('add/', views.addtask, name="addtask"),
    path('view/<int:task_id>/', views.viewtask, name='viewtask'),
    path('edit/<int:task_id>/', views.edit_task, name="edit_task"),
    path('delete/<int:task_id>/', views.delete_task, name="delete_task"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)