from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .forms import CreateTicket, AddComment
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Ticket
from django.contrib import messages
from django.db.models import Q



@login_required
def console(request):
    user = request.user
    if user.is_staff:
        return render(request, 'staff_console.html')
    else:

        open_tickets = Ticket.objects.filter(Q(creator=user) | Q(status='open')).order_by('-created_on')
        closed_tickets = Ticket.objects.filter(Q(creator=user) | Q(status='closed')).order_by('-created_on')

        context = {
            'open_tickets': open_tickets,
            'closed_tickets': closed_tickets,
        }
        return render(request, 'console.html', context)
    


@login_required
@csrf_exempt
def create_ticket(request):
    user = request.user
    if user.is_staff == False:
        if request.method == 'POST':
            form = CreateTicket(request.POST)
            if form.is_valid():
                ticket = form.save(commit=False)
                ticket.creator = request.user
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