from LendApp import *
from flask import request
from db_connect import *

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

    insert_transaction = '''Insert into transactions values ({},'{}','{}',{})'''.format(transactionid, sender, receiver, amount)

    query = db_execute(insert_transaction)
    return query


