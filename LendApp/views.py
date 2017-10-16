from LendApp import *
from flask import request, render_template
from LendApp.stripe_modules import card, charge, payout
from LendApp import db
from models import Transaction

@app.route('/')
def index():
    return 'Lend App'


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

    #print stripe.Token.retrieve(card_token)
    return generate_charge(card_token, amount, description, receipt_email)


def generate_charge(token, amount, description, receipt_email):
    generate = charge.charge_token(amount, description, receipt_email, token)
    ch_token = generate.generate_charge_token()

    tran = Transaction(id=ch_token['id'], amount=ch_token['amount'], receipt_email=ch_token['receipt_email'])
    db.session.add(tran)
    db.session.commit()

    print ch_token['id']
    return ch_token['id']


@app.route('/customer_payout')
def customer_payout():
    account_number = request.args.get('account_number')
    routing_number = request.args.get('routing_number')
    country = request.args.get('country')
    currency = request.args.get('currency')
    name = request.args.get('name')

    bank_id = payout.bank(account_number, routing_number, country, currency, name)
    bank = bank_id.create_customer()

    print bank
    return bank['id']
