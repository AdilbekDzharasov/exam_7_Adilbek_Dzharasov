from django.shortcuts import render
from webapp.models import Entry, StatusChoices


def home_view(request):
    entries = Entry.objects.filter(status=StatusChoices.ACTIVE).order_by('-created_at')
    context = {
        "entries": entries,
        "choices": StatusChoices.choices
    }
    return render(request, "home.html", context)


