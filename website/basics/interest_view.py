from django.shortcuts import render
from django.http import HttpResponse

def interest(request):
    if 'amount' in request.GET:
        amount=float(request.GET['amount'])
        rate=float(request.GET['rate'])
        interest=float(amount*rate/100)
        return render(request,'interest.html',{'amount':amount, 'rate':rate, 'interest':interest})
        # since we used required in interest.html file in form input for amount and rate "else" below won't execute
    else:
        return render(request,'interest.html')