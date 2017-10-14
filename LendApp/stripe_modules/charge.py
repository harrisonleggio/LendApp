import stripe

class charge_token():

    def __init__(self, amount, description, receipt_email, token):
        self.amount = amount
        self.description = description
        self.receipt_email = receipt_email
        self.token = token

        stripe.api_key = 'sk_test_6zvC0J40crBpuNmGBIapguU3'

    def generate_charge_token(self):
        generate = stripe.Charge.create(
            amount=self.amount,
            currency='usd',
            source=self.token,
            description=self.description,
            receipt_email=self.receipt_email
        )

        return generate
