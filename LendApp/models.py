from LendApp import db

class Transaction(db.Model):
    id = db.Column(db.String(80), primary_key=True)
    amount = db.Column(db.Integer)
    receipt_email = db.Column(db.String(80))

    def __repr__(self):
        return 'Transaction ID: {}'.format(self.transactionID)