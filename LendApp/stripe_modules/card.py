import stripe

class card_token:

    def __init__(self, number, exp_month, exp_year, cvc):
        self.number = number
        self.exp_month = int(exp_month),
        self.exp_year = int(exp_year),
        self.cvc = cvc

        stripe.api_key = 'sk_test_6zvC0J40crBpuNmGBIapguU3'

    def card_token(self):
        generate = stripe.Token.create(
            card = {
            'number': self.number,
            'exp_month': self.exp_month[0],
            'exp_year': self.exp_year[0],
            'cvc': self.cvc }
        )

        c_token = generate['id']
        return c_token
