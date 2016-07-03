from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import Http404
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from CC_app.models import CreditCard
@method_decorator(login_required,name='dispatch')
class CCListView(ListView):
    model = CreditCard
    context_object_name = "creditcard"

    def get_queryset(self):
        return CreditCard.objects.filter(user=self.request.user)

    template_name = "CC_app/CCListview.html"


@method_decorator(login_required,name='dispatch')
class CCDetailView(DetailView):
    model = CreditCard
    context_object_name = "name"
    def get_object(self, queryset=None):
         id_val = self.kwargs.get("pk")
         i=CreditCard.objects.get(id=id_val)
         j=i.user
         id2=self.request.user
         if j==id2:
             return CreditCard.objects.get(id=id_val)
         else:
             raise Http404("you are not authenticated user")

@method_decorator(login_required,name='dispatch')
class CCCreateView(CreateView):
    model=CreditCard
    fields = ['name','expDate','type','friendlyName','cardNumber']

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(CCCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("cc-list")

@method_decorator(login_required,name='dispatch')
class CCUpdateView(UpdateView):
    model=CreditCard
    fields = ['name', 'expDate', 'type', 'friendlyName', 'cardNumber']

    def get_object(self, queryset=None):
        # return super(CCUpdateView, self).get_object(queryset)
        id_val = self.kwargs.get("pk")
        i = CreditCard.objects.get(id=id_val)
        j = i.user
        id2 = self.request.user
        if j == id2:
            return CreditCard.objects.get(id=id_val)
        else:
            raise Http404("you are not authenticated user")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CCUpdateView, self).form_valid(form)

    # def get_queryset(self):
    #     return super(CCUpdateView, self).get_queryset()

    def get_success_url(self):
        return reverse("cc-list")


@method_decorator(login_required, name='dispatch')
class CCDeleteView(DeleteView):
    model = CreditCard

    def get_object(self, queryset=None):
        # return super(CCUpdateView, self).get_object(queryset)
        id_val = self.kwargs.get("pk")
        i = CreditCard.objects.get(id=id_val)
        j = i.user
        id2 = self.request.user
        if j == id2:
            return CreditCard.objects.get(id=id_val)
        else:
            raise Http404("you are not authenticated user")

    def get_success_url(self):
        return reverse("cc-list")
