"""Animal_Shelter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from shelter_app.views import RegistrationView, AnimalsView, NewAnimalView, UpdateAnimalView, IndexView, \
    animal_detail, AdmissionView, OutcomeView, HealthCareView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', IndexView.as_view()),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login_form.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('animals/', AnimalsView.as_view(), name='animals'),
    path('animals/new_animal/', NewAnimalView.as_view(), name='new_animal'),
    path('animals/<int:animal_id>/', animal_detail, name='animal'),
    path('animals/<int:animal_id>/update/', UpdateAnimalView.as_view(), name='update_animal'),
    path('animals/<int:animal_id>/admission/', AdmissionView.as_view(), name='admission'),
    path('animals/<int:animal_id>/outcome/', OutcomeView.as_view(), name='outcome'),
    path('animals/<int:animal_id>/healthcare/', HealthCareView.as_view(), name='health'),
]
