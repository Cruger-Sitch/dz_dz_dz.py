from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index_peg, name='index_peg')

]
