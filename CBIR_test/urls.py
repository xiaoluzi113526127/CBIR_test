"""CBIR_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from CBIR import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^CBIR_1/', views.sayHello),
    url(r'^CBIR_2/$', views.showInformation),
    # url(r'^site_media/(?P<path>.*)', 'django.views.static.serve', {'document_root': '/home/st/ImageNet/ILSVRC2012/ILSVRC2012/ILSVRC2012_img_train/n01440764/n01440764_18.JPEG'}),

]
