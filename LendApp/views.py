from LendApp import *
from flask import request
from LendApp.stripe_modules import card, charge
import stripe

@app.route('/')
def index():
    return 'hello world'

@app.route('/transaction')
def process_transaction():
    sender = request.args.get('sender')
    receiver = request.args.get('receiver')
    amount = request.args.get('amount')
    transactionid = request.args.get('transactionid')

    output_vals = 'Sender: {} Receiver: {} Amount: {} TransactionID: {}'.format(sender, receiver, amount, transactionid)

    return output_vals


@app.route('/card_token')
def generate_card_token():
    number = request.args.get('number')
    exp_month = request.args.get('exp_month')
    exp_year = request.args.get('exp_year')
    cvc = request.args.get('cvc')

    amount = request.args.get('amount')
    description = request.args.get('description')
    receipt_email = request.args.get('receipt_email')

    generate = card.card_token(number, exp_month, exp_year, cvc)
    card_token = generate.generate_card_token()

    print stripe.Token.retrieve(card_token)
    return generate_charge(card_token, amount, description, receipt_email)


def generate_charge(token, amount, description, receipt_email):
    generate = charge.charge_token(amount, description, receipt_email, token)
    ch_token = generate.generate_charge_token()

    print ch_token
    return ch_token['id']

