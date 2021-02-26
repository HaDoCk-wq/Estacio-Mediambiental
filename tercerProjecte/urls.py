"""tercerProjecte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

######## API #########
from estaciOmediambiental.views import ClientViewSet, SensorViewSet, RegistreViewSet

######## Views #########
from estaciOmediambiental.views import test, xhr, dades


router = routers.DefaultRouter()
router.register('Clients', ClientViewSet)
router.register('Sensors', SensorViewSet)
router.register('Registre', RegistreViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),

    ###### API ######
    path('docs/', include_docs_urls(title='Django', public=False)),
    path('api/', include(router.urls)),

    ##### Views ######
    path('test', test.as_view()),
    path('xhr', xhr.as_view()),
    path('dades', dades.as_view())
]
