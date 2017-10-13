from LendApp import *
from flask import request
import dwollav2

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

