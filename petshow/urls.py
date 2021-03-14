from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login', views.LoginView.as_view(), name="login"),
    path('profile/', views.profile, name="profile"),
    path('shows', views.ShowsView.as_view(), name="shows"),
    path('shows/dogshow', views.dogshow, name="dogshow"),
    path('shows/catshow', views.catshow, name="catshow"),
    path('shows/add_pet', views.CreatePetOnShow.as_view(), name="add_pet"),
    path('shows/mypets', views.mypets, name="mypets"),
    path('shows/add/<slug:slug>', views.start_show, name="start_show"),
    path('shows/stop/<slug:slug>', views.stop_show, name="stop_show"),
    path('vote_plus/<int:pet_id>', views.vote_plus, name="vote_plus"),
    path('vote_minus/<int:pet_id>', views.vote_minus, name="vote_minus"),
    path('article/', views.articles, name="article"),
    path('article/<int:article_id>/', views.detail, name ='detail'),
    path('about_us/', views.AboutUsView.as_view(), name="about_us"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('contact/', views.contactform, name='contact'),
    path('thanks/', views.thanks, name='thanks'),
]