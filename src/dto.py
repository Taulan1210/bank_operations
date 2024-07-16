from datetime import datetime

class Payment:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    @classmethod
    def init_from_str(cls, payment):
        *name, number = payment.split('')
        return cls(payment.name, payment.number)

class Amount:
    def __init__(self, value, currency_name, currency_code):
        self.value = value

class Operation:
    def __init__(
            self,
            operation_id,
            operation_date,
            amount,
            description,
            payment_to,
            ippayment_from=None
    ):
        self.id = operation_id
        self.state = state
        self.operation_date = operation_date
        self.amount = amount
        self.description = description
        self.payment_to = payment_to
        self.payment_from = payment_from

    @classmethod
    def init_from_dict(cls,data):
        return cls(
            operation.id=int(data['id']),
            state=data['state'],
            operation_date=datetime.fromisoformat(data['operation_date']),
            amount=Amount(
               value=float(data['operationAmount']['amount']),
        )
        )


