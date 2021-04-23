from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Authentication
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .models import Quote
from .forms import QuoteForm
from pages.models import Page


# User Registration
class Register(CreateView):
    # properties assignment
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')
    # method
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


class QuoteListView(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    #model = Quote
    context_object_name = 'all_quotes' # naaming the object that will be passed over to the template

    # Mixins
    # Only extract the list of quotes for the currently logged-in user
    def get_queryset(self):
        return Quote.objects.filter(username = self.request.user)
    # Mixins
    def get_context_data(self, **kwargs):
        context = super(QuoteListView, self).get_context_data(**kwargs)
        context['page_list'] = Page.objects.all()
        return context

class QuoteDetailView(LoginRequiredMixin,DetailView):
    login_url = reverse_lazy('login')
    #model = Quote
    context_object_name = 'quote'

    #Mixin
    # Only extract the individual quote for current logged-in user
    def get_queryset(self):
        return Quote.objects.filter(username = self.request.user)
    
    # Mixin
    def get_context_data(self, **kwargs):
        context = super(QuoteDetailView, self).get_context_data(**kwargs)
        context['page_list'] = Page.objects.all()
        return context

@login_required(login_url=reverse_lazy('login')) # prevent unauthorized access
def quote_req(request):
    submitted = False
    if request.method == 'POST':
        form = QuoteForm(request.POST, request.FILES)
        if form.is_valid():
            quote = form.save(commit=False)
            try:
                quote.username = request.user
            except Exception:
                pass
            quote.save()
            return HttpResponseRedirect('/quote/?submitted=True')
    else:
        form = QuoteForm()
        if 'submitted' in request.GET:
            submitted = True
    context = {
        'form' : form,
        'page_list' : Page.objects.all(),
        'submitted' : submitted
    }
    return render(request, 'quotes/quote.html', context)
    