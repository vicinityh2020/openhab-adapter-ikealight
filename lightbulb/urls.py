from django.urls import path

from . import views

urlpatterns = [
    path('objects', views.thing_descriptor, name='objects_view'),
    path('devices/<oid>/properties/<pid>', views.lightbulb_color, name='lightbulb_color_view')
]
