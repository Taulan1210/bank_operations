from datetime import datetime


class Payment:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __repr__(self):
        return f'Payment(name={self.name}, number={self.number}'

    @classmethod
    def init_from_str(cls, payment):
        *name, number = payment.split('')
        return cls(''.join(name), number)

    def safe(self) -> str:
        if self.name.lower() == 'счет':
            safe_number = self.__get_safe_account()
        else:
            safe_number = self._get_safe_card_number()
        return f'{self.name} {self.number})'

class Amount:
    def __init__(self, value, currency_name, currency_code):
        self.value = value
        self.currency_name = currency_name
        self.currency_code = currency_code

    def __repr__(self):
        return f'Amount(value={self.value}, currency_name={self.currency_name}'

class Operation:
    def __init__(
            self,
            operation_id,
            state,
            operation_date,
            amount,
            description,
            payment_to,
            payment_from=None
    ):
        self.id = operation_id
        self.state = state
        self.operation_date = operation_date
        self.amount = amount
        self.description = description
        self.payment_to = payment_to
        self.payment_from = payment_from

    def __repr__(self):
        return (
            f'Operation('
            f'{self.id}, {self.description}, state={self.state}, date={self.operation_date}, amount={self.amount}'
            f'from={self.payment_from}, to={self.payment_to}'
            f')'
        )

    @classmethod
    def init_from_dict(cls,data: dict):
        return cls(
            operation_id=int(data['id']),
            state=data['state'],
            operation_date=datetime.fromisoformat(data['operation_date']),
            amount=Amount(
               value=float(data['operationAmount']['amount']),
               currency_name=data['operationAmount']['currency']['name'],
               currency_code=data['operationAmount']['currency']['code']
            ),
            description=data['description'],
            payment_to=Payment.init_from_str(data['to']),
            payment_from=Payment.init_from_str(data['from']) if 'from' in data else None
        )


