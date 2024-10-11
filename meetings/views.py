from django.shortcuts import render

from .models import Meeting
from django.shortcuts import get_object_or_404


# Create your views here.

def meetings_list_view(request):

    meetings = Meeting.objects.all()  # Get all meetings

    return render(request, 'meetings.html', {'meetings': meetings, })


def detail(request, id):

    meeting = get_object_or_404(Meeting, id=id)  # Correct model name and function

    return render(request, "details.html", {"meeting": meeting})