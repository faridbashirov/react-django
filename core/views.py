from django.shortcuts import render
from core.forms import ContactForm
from django.forms import inlineformset_factory,formset_factory
from core.models import Blogs,Contact


def index(request, *args, **kwargs):
    form=formset_factory()
    form=inlineformset_factory(Contact,extra=5)
    blogs=Blogs.objects.all()

    context={
        "form":form,
        "blogs":blogs


    }

    return render(request, 'index.html',context)