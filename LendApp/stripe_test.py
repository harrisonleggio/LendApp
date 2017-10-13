import stripe

# test stripe API key
stripe.api_key = 'sk_test_6zvC0J40crBpuNmGBIapguU3'

# generating a credit card token to charge
tok = stripe.Token.create(
    card={
    "number": '4242424242424242',
    "exp_month": 12,
    "exp_year": 2018,
    "cvc": '123'}
    )

# storing the ID of the token
id_token = tok['id']

# creating a charge and passing the previous card token
test_charge = stripe.Charge.create(
    amount=100,
    currency='usd',
    source=id_token,
    description='test',
    receipt_email='harrisonleggio@my.uri.edu'
)

# output of test charge
print test_charge