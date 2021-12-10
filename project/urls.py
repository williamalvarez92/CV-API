"""project URL Configuration

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
from django.urls import path, re_path
from about.views import AboutListView
from education.views import EducationListView
from portfolio.views import PortfolioListView
from skill.views import SkillsListView
from social.views import SocialsSerializer
from work_history.views import WorkListView

from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cv/about/', AboutListView.as_view(), name='about'),
    path('cv/education/', EducationListView.as_view(), name='education'),
    path('cv/portfolio/', PortfolioListView.as_view(), name='portfolio'),
    path('cv/skills/', SkillsListView.as_view(), name='skills'),
    path('cv/social/', SocialsSerializer.as_view(), name='social'),
    path('cv/work/', WorkListView.as_view(), name='work'),
    re_path(r'^.*$', index) 
]