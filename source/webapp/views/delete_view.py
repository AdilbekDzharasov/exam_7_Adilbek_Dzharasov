from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Entry


def delete_entry(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'entry': entry})
    elif request.method == 'POST':
        entry.delete()
        return redirect('home')

