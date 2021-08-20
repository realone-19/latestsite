from django.urls import path
from customer.views import CustomerDetailView, PaymentListView, CustomerIndexView
from customer import views


app_name = 'customer'

urlpatterns = [
    path('', views.user_login,name='user_login'),
    path('user_login', views.user_login,name='user_login'),
    path('customer_index', CustomerIndexView.as_view(),name='customer_index'),
    path('detail/<int:pk>/',CustomerDetailView.as_view(),name='detail'),
    path('payment',PaymentListView.as_view(),name='payment'),
]
