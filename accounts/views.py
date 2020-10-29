from django.contri.auth.forms import UserCreationForm
from django.urls import reserve_lazy
from django.views import generic

class SighnUpView(generic.CreateView):
    from_class =UserCreationFormsuccess_url