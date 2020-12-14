class Transaction:

    def __init__(self, amount, merchant, tag, id=None):
        self.amount = amount 
        self.merchant = merchant
        self.tag = tag
        self.id = id

    def convert_to_pennies(self):
        self.amount = float(self.amount) * 100

    def convert_to_pounds(self, amount_as_pennies):
        return amount_as_pennies / 100
        

