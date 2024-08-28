from datetime import date
from typing import List, Callable, Optional


class Customer:
    def __init__(self, first_name: str, last_name: str, birthday: date):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday

    def full_name(self) -> str:
        return f"{self.first_name.lower()} {self.last_name}"

    def email(self) -> str:
        return f"{self.first_name.lower()}.{self.last_name.lower()}@mybank.com"


class CustomerService:
    def __init__(self):
        self.customers: List[Customer] = []

    def add_customer(self, first_name: str, last_name: str, birthday: date) -> None:
        if not first_name or not last_name:
            raise ValueError("Mandatory name parameter is missing")

        if self.customer_exists(first_name, last_name):
            raise ValueError("Customer already exists")

        self.customers.append(Customer(first_name, last_name, birthday))

    def customer_exists(self, first_name: str, last_name: str) -> bool:
        if not self.customers:
            return False

        return any(self.has_same_name(customer, first_name, last_name) for customer in self.customers)

    def remove_customer(self, first_name: str, last_name: str, birthday: date) -> None:
        self.customers = [
            customer for customer in self.customers
            if not (self.has_same_name(customer, first_name, last_name) and customer.birthday == birthday)
        ]

    def search_customer(self, first_name: str, last_name: str) -> Optional[Customer]:
        customers = self.search_customers(first_name, last_name)
        return customers[0] if customers else None

    def search_customers(self, first_name: str = None, last_name: str = None) -> List[Customer]:
        if first_name is None or last_name is None:
            return self._search_customers(lambda customer: True)
        else:
            return self._search_customers(lambda customer: self.has_same_name(customer, first_name, last_name))

    def _search_customers(self, match: Callable[[Customer], bool]) -> List[Customer]:
        return [customer for customer in self.customers if match(customer)]

    @staticmethod
    def has_same_name(customer: Customer, first_name: str, last_name: str) -> bool:
        return customer.first_name == first_name and customer.last_name == last_name
