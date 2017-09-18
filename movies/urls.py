from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^add_film/$', views.add_film, name='add_film'),
    url(r'^(?P<genre>[-\w.]+)/$', views.genre_page, name='genre_page'),
    url(r'^detail/(?P<slug>[-\w.]+)/$', views.movie_detail, name='detail'),
]
