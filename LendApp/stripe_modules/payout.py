import stripe

class bank:

    def __init__(self, account_number, routing_number, country, currency, name):
        self.account_number = account_number
        self.routing_number = routing_number
        self.country = country
        self.currency = currency
        self.name = name

        stripe.api_key = 'sk_test_6zvC0J40crBpuNmGBIapguU3'

    def create_customer(self):
        customer_id = stripe.Customer.create(
            description = self.name
        )
        customer = stripe.Customer.retrieve(customer_id['id'])

        bank = customer.sources.create(
            bank_account = {
                'account_number': self.account_number,
                'routing_number': self.routing_number,
                'account_holder_type': 'individual',
                'account_holder_name': self.name,
                'country': self.country,
                'currency': self.currency }
        )

        return bank


# MUST USE BELOW VALUES FOR TESTING:
# account_number = '000123456789'
# routing_number = '110000000'
