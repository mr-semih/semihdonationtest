from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

import stripe
stripe.api_key = "sk_test_51K4rWLEv5TNMLd7w2jI6cjLc0fAZIVvEdnUCFMNNVvGNzILVCTXZjvJbUxz2DPyZ1XW2breMqikA9yQ0quwMnMDe00k2VZigIU"

# Create your views here.

def index(request):

	return render(request, 'base/index.html')


def charge(request):


	if request.method == 'POST':
		print('Data:', request.POST)

		amount = int(request.POST['amount']) # html formumun gönderdiği amount bilgisini amount variable ında kaydediyoruz.

		customer = stripe.Customer.create( # bu kısım stripe.com da customers kısmına gittiğimizde orada customer objeleri oluşturmamızı ve buradaki bilgileri oraya kaydetmemizi sağlıyor.
			email=request.POST['email'],
			name=request.POST['nickname'],
			source=request.POST['stripeToken'] # bu charge edilecek kaynaktır. kredi kartı, debit kard gibi ...
			)

		charge = stripe.Charge.create( # bu kısım stripe.com da customer kısmına gittiğimizde orada payment objeleri oluşturmamızı ve buradaki bilgileri oraya kaydetmemizi sağlıyor.
			customer=customer, # customer yukarıda oluşturduğumuz customer variable
			amount=amount*100, # belirttiğimiz amount penny cinsinden yani 2000 penny = 20 dolar. buradaki amount variable yukarıda tanımladığımız variable
			currency='usd',
			description="Donation" # bu stripe.com da açıklama olarak gözükecek
			)

	return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
	amount = args
	return render(request, 'base/success.html', {'amount':amount})