from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.signin, name='post_list'),
    path('Index/', views.BookList.as_view(), name='Index'),
    path('Fantasy/',views.FantasyList.as_view(),name='Fantasy'),
    path('Formazione/',views.RomanziList.as_view(),name='Formazione'),
    path('Tutti/',views.TuttiList.as_view(),name='Tutti'),
    path('Gialli/',views.GialliList.as_view(),name='Gialli'),
] 

urlpatterns += staticfiles_urlpatterns()