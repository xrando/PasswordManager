from django.urls import path

from . import views

urlpatterns = [
    # path("login/", views.login_view, name="login"),
    # path("logout/", views.logout_view, name='logout'),
    # path("register/", views.register, name='register'),
    path("", views.index, name="index"),
    path("create/", views.create, name='create'),
    path("view/<int:entry_id>", views.view, name='view'),
    path("edit/<int:entry_id>", views.edit, name='edit'),
    path("delete/<int:entry_id>", views.delete, name='delete'),
]
