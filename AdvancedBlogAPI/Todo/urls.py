from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add/$', views.addTodo, name="add"),
    url(r'^complete/(?P<todo_id>\d+)/$', views.completeTodo, name="complete"),
    url(r'^deletecomplete/$', views.deleteCompleted, name="deletecomplete"),
    url(r'^deleteall/$', views.deleteAll, name="deleteall")
]
