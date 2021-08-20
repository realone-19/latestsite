from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from customer.models import Customer, Account_detail
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from customer.models import Customer, Account_detail

# Create your views here.
# @login_required(login_url='/customer/user_login/')
class CustomerIndexView(TemplateView):
    template_name = "customer/customer_index.html"



class CustomerDetailView(DetailView):
    model = Customer


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['max_value'] = 100
        return context


# class PaymentListView(ListView):
#     model = Account_detail
#
#     def get_queryset(self):
#         queryset = Account_detail.objects.filter(customer__full_name='{} {}'.format(self.request.user.first_name,
#                                                                                             self.request.user.last_name).upper())
#         return queryset


# @login_required(login_url='/customer/user_login/')
class PaymentListView(ListView):
    model = Account_detail


    def get_queryset(self):        
        queryset = Account_detail.objects.filter(customer__full_name='{} {}'.format(self.request.user.first_name,
                                                                                            self.request.user.last_name).upper()).order_by('-date')
        return queryset

# def register(request):
#     registered = False
#     user_form = forms.UserForm()
#     profile_form = forms.UserProfileForm()
#
#     if request.method == 'POST':
#         user_form = forms.UserForm(data=request.POST)
#         profile_form = forms.UserProfileForm(data=request.POST)
#         if user_form.is_valid:
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()
#
#             profile = profile_form.save(commit=False)
#             profile.user = user
#
#             if 'phone_number' in request.POST:
#                 profile.phone_number = request.POST['phone_number']
#                 profile.save()
#
#             registered = True
#             return HttpResponseRedirect('user_login')
#         else:
#             print(user_form.errors)
#
#     else:
#         return render(request,'customer_info/registration.html',{'user_form':user_form,
#                                                             'profile_form':profile_form,
#                                                             'registered':registered})



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                # return HttpResponseRedirect(reverse('customer_index'))
                return HttpResponseRedirect('customer_index')
            else:
                return HttpResponse('Account not active')
        else:
            return render(request, 'customer/user_login.html')

    else:
        return render(request, 'customer/user_login.html')
