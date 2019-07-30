"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url # changed from path to url

from django.urls import include, path
#from controlcenter.views import controlcenter

from boards import views #added

urlpatterns = [
    url(r'^$', views.home, name='home'), # added; path or url?
    # url(r'^admin/', admin.site.urls),  # added
    url(r'^donors/(?P<pk>\d+)/$', views.donationsinfo, name='donationsinfo'),
    url(r'^donors/(?P<pk>\d+)/new/$', views.new_donations, name='new_donations'),
    url(r'^admin/', admin.site.urls),  # this is the original

    #url(r'^admin/dashboard/', controlcenter.urls),
    url(r'^tasks/', include('tasks.urls'))
    url(r'^donors/(?P<pk>\d+)/detail/$', views.detail_info, name='detail_info')

]

# so this one works, i don't know why
