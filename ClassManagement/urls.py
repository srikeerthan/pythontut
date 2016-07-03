"""ClassManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin
from  CC_app import ClassView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'my/creditcards/$',ClassView.CCListView.as_view(),name="cc-list"),
    url(r'my/creditcards/(?P<pk>[0-9]+)/details/$', ClassView.CCDetailView.as_view()),
    url(r'my/creditcards/create',ClassView.CCCreateView.as_view()),
    url(r'my/creditcards/(?P<pk>[0-9]+)/update', ClassView.CCUpdateView.as_view()),
    url(r'my/creditcards/(?P<pk>[0-9]+)/delete', ClassView.CCDeleteView.as_view()),
    # url(r'^login/$', 'django.contrib.auth.views.login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout'),
]
