from django.urls import path
from webapp.views.base import home_view
from webapp.views.add import add_view
from webapp.views.update_view import update_entry
from webapp.views.delete_view import delete_entry


urlpatterns = [
    path('', home_view, name='home'),
    path('entry/add/', add_view, name='entry_add'),
    path('entry/update/<int:pk>', update_entry, name='entry_update'),
    path('entry/delete/<int:pk>', delete_entry, name='entry_delete'),
]


