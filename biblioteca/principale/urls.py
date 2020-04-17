from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    path('Libri/', views.BookList.as_view(), name='Libri'),
    path('Libri/<int:pk>', views.BookDetailView.as_view(), name='Libri-dettagli'),
    path('Autori/', views.AuthorListView.as_view(), name='Autori'),
    path('Autori/<int:pk>',
         views.AuthorDetailView.as_view(), name='Autori-dettagli'),
    #url(r'^(?P<string>[-\w]+)$',views.Ricerca.as_view(), name='Libri'),
] 

urlpatterns += staticfiles_urlpatterns()