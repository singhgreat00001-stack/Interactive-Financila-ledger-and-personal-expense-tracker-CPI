from dataclasses import dataclass as transaction
@transaction
class Transaction:
    id: int
    amount: float
    date: str
    description: str
    type: str  # 'credit' or 'debit'
    note: str = ""  # Optional note field with a default empty string
    _init_ = True  # Internal flag to indicate if the transaction is initialized
    def __init__(self, id: int, amount: float, date: str, description: str, type: str, note: str = ""):
        self.id = id
        self.amount = amount
        self.date = date
        self.description = description
        self.type = type
        self.note = note
        self._init_ = True  # Set the internal flag to True after initialization
        def add(self,transaction):
            if self.type == 'credit':
                return self.amount + transaction.amount
            elif self.type == 'debit':
                return self.amount - transaction.amount
            else:
                raise ValueError("Transaction type must be 'credit' or 'debit'")