class ExpenseTracker:
    def __init__(self):
        self.transactions = []

    def add_expense(self, expense):
        self.transactions.append(expense)

    def total_expense(self):
        sum = 0
        for transaction in self.transactions:
            sum += transaction

        return sum
    
e = ExpenseTracker()
e.add_expense(200)
e.add_expense(300)
print(e.total_expense())