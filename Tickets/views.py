from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import CreateTicket
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


@login_required
@csrf_exempt
def create_ticket(request):
    user = request.user
    if user.is_staff == False:
        if request.method == 'POST':
            form = CreateTicket(request.POST)
            if form.is_valid():
                form.instance.creator = request.user
                ticket = form.save()
                ticket.save()

                return redirect('console')
        else:
            form = CreateTicket()
        return render(request, 'create_ticket.html', {'form': form})
    else:
        return HttpResponse("You cannot perform this action!") # This bars members of staff from creating tickets.
    
