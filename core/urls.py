from django.urls import path
from . import views
from .views import (
    UserRegistrationView,
    UserView,
    AllUsersView,
    UserLoginView,
    UserLogoutView,
    UserProfileView,
    BookListCreateView,
    BookRetrieveUpdateDestroyView
)

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('user/<int:pk>/', UserView.as_view(), name='user'),
    path('users/', AllUsersView.as_view(), name='all-users'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user-profile'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),

]