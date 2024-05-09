from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.utils.text import slugify
from django.db import IntegrityError

from customer.models import Customer

def index(request):
    customers = Customer.objects.all()
    customer = None

    if 'customer' in request.GET:
        customer = Customer.objects.filter(slug=request.GET.get('customer')).first()

    context = {
        'customers': customers,
        'customer': customer
    }

    if request.method == 'POST':
        sender_name = request.POST['sender_name']
        sender_address = request.POST['sender_address']
        sender_phone = request.POST['sender_phone']
        recepient_name = request.POST['recepient_name']
        recepient_address = request.POST['recepient_address']
        recepient_phone = request.POST['recepient_phone']

        if len(recepient_phone) < 10:
            messages.add_message(request, messages.ERROR, 'Jumlah nomor HP tidak benar')
            return render(request, 'index.html')
        
        if recepient_phone[0]+''+recepient_phone[1] != '62':
            messages.add_message(request, messages.ERROR, 'Format nomor HP harus diawali 62')
            return render(request, 'index.html')
        
        try:
            customer = Customer()
            customer.name = request.POST['recepient_name']
            customer.slug = slugify(f"{request.POST['recepient_name']}-{request.POST['recepient_phone']}-{request.POST['recepient_address']}")
            customer.phone = request.POST['recepient_phone']
            customer.address = request.POST['recepient_address']
            customer.save()
        except:
            pass
        
        return HttpResponseRedirect(
            reverse("detail", kwargs={
                    "sender_name": sender_name,
                    "sender_phone": sender_phone,
                    "sender_address": sender_address,
                    "recepient_name": recepient_name,
                    "recepient_phone": recepient_phone,
                    "recepient_address": recepient_address
                }
            )
        )
    
    return render(request, 'index.html', context=context)

def detail(request, sender_name, sender_phone, sender_address, recepient_name, recepient_phone, recepient_address):
    
    context = {
        'sender_name': sender_name,
        'sender_address': sender_address,
        'sender_phone': sender_phone,
        'recepient_name': recepient_name,
        'recepient_address': recepient_address,
        'recepient_phone': recepient_phone,
    }

    return render(request, 'detail.html', context=context)