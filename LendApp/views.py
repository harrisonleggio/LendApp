from LendApp import *
from flask import request
from LendApp.stripe_modules import card

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

    generate = card.card_token(number, exp_month, exp_year, cvc)
    c_token = generate.card_token()

    return c_token



