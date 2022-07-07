from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fake', views.fake, name='fake'),
    #path('test', views.test_post.as_view())
]
