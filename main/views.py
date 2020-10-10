# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import stripe

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

stripe.api_key = 'sk_test_lTCPKBSdIQX4eSO9meZUIgkk'


def index(request):

    if request.method == "POST":
        stripe.PaymentIntent.confirm(request.POST.get('client_secret'), payment_method="pm_card_visa")
        return HttpResponse("hey")
    intent = stripe.PaymentIntent.create(
        amount=1099,
        currency='usd',
        metadata={'integration_check': 'accept_a_payment'},
        payment_method_types=["card"]
    )
    context = {'client_secret': intent.client_secret}
    return render(request, 'main/index.html', context)


def confirm_order(request):
    result_id = request.GET.get('result_id', None)
    writer = open("Orders.txt", str("a"))
    writer.write(result_id + "\n")
    writer.close()

    return JsonResponse({})
