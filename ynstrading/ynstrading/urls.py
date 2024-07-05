"""
URL configuration for ynstrading project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name='homePage'),
    path('mens/', views.mens_products, name='mens_products'),
    path('womens/', views.womens_products, name='womens_products'),
    path('tanktops/', views.tanktop_products, name='tanktop_products'),
    path('swimwear/', views.swimwear_products, name='swimwear_products'),
    path('sundress/', views.sundress_products, name='sundress_products'),
    path('bright/', views.bright_products, name='bright_products'),
    path('heavycoat/', views.heavycoat_products, name='heavycoat_products'),
    path('gloves/', views.gloves_products, name='gloves_products'),
    path('hats/', views.hats_products, name='hats_products'),
    path('thermal/', views.thermal_products, name='thermal_products'),
    path('longsleeves/', views.longsleeves_products, name='longsleeves_products'),
    path('sweaters/', views.sweaters_products, name='sweaters_products'),
    path('jeans/', views.jeans_products, name='jeans_products'),
    path('fall/', views.fall_products, name='fall_products'),
    path('summer/', views.summer_products, name='summer_products'),
    path('winter/', views.winter_products, name='winter_products'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)