from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from home.models import Lead
from home.models import Product
from home.forms import LeadForm

# Create your views here.


class IndexView(TemplateView):
    template_name = "home/index.html"


class ProductListView(ListView):
    model = Product


    def get_queryset(self):
        queryset = Product.objects.order_by('price')
        return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['form'] = LeadForm()
        return context



class LeadView(CreateView):
    model = Lead
    fields = '__all__'
    # success_url = reverse_lazy('/index')
    success_url = '/index'



def register_lead(request):
    form = LeadForm()
    # return render(request, 'product_list.html', {'form': form})

        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LeadForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LeadForm()

    return render(request, 'index.html', {'form': form})
