from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .forms import CreateTicket, AddComment
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Ticket
from django.contrib import messages


@login_required
@csrf_exempt
def create_ticket(request):
    user = request.user
    if user.is_staff == False:
        if request.method == 'POST':
            form = CreateTicket(request.POST)
            if form.is_valid():
                form.instance.creator = user
                ticket = form.save()
                ticket.save()

                return redirect('console')
        else:
            form = CreateTicket()
        return render(request, 'create_ticket.html', {'form': form})
    else:
        return HttpResponse("You cannot perform this action!") # This bars members of staff from creating tickets.
    


@login_required
@csrf_exempt
def add_comment(request, id):
    user = request.user
    ticket = Ticket.objects.get(id=id)
    if ticket.status == 'Open':
        if request.method == 'POST':
            form = AddComment(request.POST)
            if form.is_valid():
                form.instance.commented_by = user
                form.instance.belongs_to_ticket = ticket
                comment = form.save()
                comment.save()
                return redirect('console')
        else:
            form = AddComment()
        return render(request, 'add_comment.html', {'form': form})
    else:
        return messages.error("This ticket is closed!")