from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import MakePaymentForm, DonationForm
from .models import Donation, DonationLineItem
from django.conf import settings
from django.utils import timezone
import stripe


# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

def donation(request):
    if request.method=="POST":
        donation_form = DonationForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if donation_form.is_valid() and payment_form.is_valid():
            donate = donation_form.save(commit=False)
            donate.date = timezone.now()
            donate.save()
            
            try:
                donator = stripe.Charge.create(
                    amount = (request.amount) * 100,
                    currency = "EUR",
                    email = request.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
                
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if donator.paid:
                messages.error(request, "Thank you for your donation!")
                return redirect(reverse('home'))
                
            else:
                messages.error(request, "Unable to take your donation")
                
        else:
            print(payment_form.errors)
            messages.error(request, "We are unable to take your donation with the card you have")
            
    else:
        donation_form = DonationForm()
        payment_form = MakePaymentForm()
    
    context = {
        'donation_form': donation_form, 
        'payment_form': payment_form, 
        'publishable': settings.STRIPE_PUBLISHABLE
    }    

    return render(request, "donation.html", context)    