from LendApp import db

class Transaction(db.Model):
    transactionID = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    sender = db.Column(db.String(80))
    receiver = db.Column(db.String(80))

    def __repr__(self):
        return 'Transaction ID: {}'.format(self.transactionID)