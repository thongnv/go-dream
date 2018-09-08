"""godream URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns


def generate_url_include(name):
    regex = r'^{}/'.format(name)
    to_include = include('{}.urls'.format(name))
    namespace = 'godream.{}'.format(name)
    return url(regex, to_include, name=namespace)


namespaces_to_include = [
    "users"
]

namespaced_urls = [
    generate_url_include(name) for name in namespaces_to_include
]

urlpatterns = [
    url(r'^api/', include(namespaced_urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL)
