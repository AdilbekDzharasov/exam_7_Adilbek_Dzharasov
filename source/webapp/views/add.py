from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Entry
from webapp.forms import EntryForm


def add_view(request):
    if request.method == "GET":
        form = EntryForm()
        return render(request, "add.html", context={'form': form})
    elif request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            entry = Entry.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                text_entry=form.cleaned_data['text_entry']
            )
            return redirect('home')
        else:
            return render(request, 'add.html', context={'form': form})

