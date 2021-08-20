from django.urls import path
from home.views import IndexView
from home.views import ProductListView, IndexView, LeadView
from home import views

app_name = 'home'

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('index',IndexView.as_view(),name='index'),
    path('products',ProductListView.as_view(),name='products'),
    # path('register',views.register_lead,name='register'),
    path('registration',LeadView.as_view(),name='registration'),
]
