from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Entry
from webapp.forms import EntryForm


def update_entries(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'GET':
        form = EntryForm(initial={
            'name': entry.name,
            'email': entry.email,
            'text_entry': entry.text_entry
        })
        return render(request, 'update.html', context={'form': form, 'entry': entry})
    elif request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            entry.name = form.cleaned_data['name']
            entry.email = form.cleaned_data['email']
            entry.text_entry = form.cleaned_data['text_entry']
            entry.save()
            return redirect('home')
        else:
            return render(request, 'update.html', context={'form': form, 'entry': entry})

