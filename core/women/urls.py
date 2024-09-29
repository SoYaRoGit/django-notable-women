from django.urls import path, register_converter

from women import converters, views

register_converter(converters.FourDigitYearConverter, type_name="year4")

urlpatterns = [
    path("", views.index),  # http://127.0.0.1:8000
    path("cats/<int:cat_id>/", views.categories),  # http://127.0.0.1:8000/cats/
    path("archive/<year4:year>/", views.archive),
]
