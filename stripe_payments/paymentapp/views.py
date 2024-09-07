
from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
import json
# Set your Stripe secret key

stripe.api_key = settings.STRIPE_PRIVATE_KEY


def index(request):
    # Just render the index page without creating a session here
    return render(request, 'myapps/index.html')

def create_checkout(request):
    # creating the Stripe checkout session

    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': 'price_1PmFP9Rx3qur0eu5DcprVgEx',
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('thanks')) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri(reverse('index')),
        )

        return JsonResponse({
            'session_id': session.id,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def thanks(request):
    return render(request, 'myapps/thanks.html')


# @csrf_exempt
# def stripe_webhook(request):

#     endpoint_secret = 'whsec_...'
#     payload = request.body
#     event = None

#     try:
#         event = stripe.Event.construct_from(
#         json.loads(payload), stripe.api_key
#         )
#     except ValueError as e:
#         # Invalid payload
#         return HttpResponse(status=400)

#     # Handle the event
#     if event.type == 'payment_intent.succeeded':
#         payment_intent = event.data.object # contains a stripe.PaymentIntent
#         # Then define and call a method to handle the successful payment intent.
#         # handle_payment_intent_succeeded(payment_intent)


#     elif event.type == 'payment_method.attached':
#         payment_method = event.data.object # contains a stripe.PaymentMethod
#         # Then define and call a method to handle the successful attachment of a PaymentMethod.
#         # handle_payment_method_attached(payment_method)
#     # ... handle other event types

        
    
#     else:
#         print('Unhandled event type {}'.format(event.type))

#     return HttpResponse(status=200)

# views.py

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return JsonResponse({'error': str(e)}, status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return JsonResponse({'error': str(e)}, status=400)

    # Handle the event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        # Fulfill the purchase...
        print(session)
        line_items = stripe.checkout.Session.list_line_items(session['id'],limit=1)
        print(line_items)
        
        handle_checkout_session(session)

        

    return JsonResponse({'status': 'success'}, status=200)


def handle_checkout_session(session):
    # Implement your logic here to fulfill the order
    print("Payment was successful!")
