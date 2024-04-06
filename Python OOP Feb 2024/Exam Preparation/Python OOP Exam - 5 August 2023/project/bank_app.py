from typing import List

from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOANS = {
        "MortgageLoan": MortgageLoan,
        "StudentLoan": StudentLoan
    }
    VALID_CLIENTS = {
        "Adult": Adult,
        "Student": Student
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[MortgageLoan, StudentLoan] = []
        self.clients: List[Adult, Student] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOANS.keys():
            raise Exception("Invalid loan type!")

        new_loan = self.VALID_LOANS[loan_type]()
        self.loans.append(new_loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENTS.keys():
            raise Exception("Invalid client type!")

        if self.capacity == len(self.clients):
            return f"Not enough bank capacity."

        new_client = self.VALID_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        searched_loan = next(filter(lambda l: l.__class__.__name__ == loan_type, self.loans), None)
        searched_client = next(filter(lambda c: c.client_id == client_id, self.clients), None)

        if searched_client.__class__.__name__ == "Student" and loan_type == "StudentLoan":
            self.loans.remove(searched_loan)  # TODO: CARE if loan not in the banks list of loans
            searched_client.loans.append(searched_loan)
            return f"Successfully granted {loan_type} to {searched_client.name} with ID {client_id}."

        elif searched_client.__class__.__name__ == "Adult" and loan_type == "MortgageLoan":
            self.loans.remove(searched_loan)  # TODO: CARE if loan not in the banks list of loans
            searched_client.loans.append(searched_loan)
            return f"Successfully granted {loan_type} to {searched_client.name} with ID {client_id}."
        else:
            raise Exception("Inappropriate loan type!")

    def remove_client(self, client_id: str):
        try:
            searched_client = next(filter(lambda c: c.client_id == client_id, self.clients))
        except StopIteration:
            raise Exception("The client has loans! Removal is impossible!")

        if len(searched_client.loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(searched_client)
        return f"Successfully removed {searched_client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):  # StudentLoan

        changed_loans = [l.increase_interest_rate() for l in self.loans if
                         l.__class__.__name__ == loan_type]  # TODO: CARE here

        return f"Successfully changed {len(changed_loans)} loans."  # TODO: CARE CARE Loans that are already granted to clients should not be affected.

    def increase_clients_interest(self, min_rate: float):

        clients_w_changed_interest = [c.increase_clients_interest() for c in self.clients if
                                      c.interest < min_rate]

        return f"Number of clients affected: {len(clients_w_changed_interest)}."

    def get_statistics(self):
        total_clients_income_list = [c.income for c in self.clients]
        total_bank_loans = [l.amount for l in self.loans]

        total_granted_to_clients_amount = 0
        count_granted_loans_count = 0
        for client in self.clients:
            for client_loan in client.loans:
                total_granted_to_clients_amount += client_loan.amount
                count_granted_loans_count += 1

        total_not_granted_list = [l.amount for l in self.loans]

        list_of_int_rates_of_clients = [c.interest for c in self.clients]

        if len(list_of_int_rates_of_clients) == 0:
            avg_client_interest_rate = 0
        else:
            avg_client_interest_rate = sum(list_of_int_rates_of_clients) / len(list_of_int_rates_of_clients)

        result = f"Active Clients: {len(self.clients)}\nTotal Income: {sum(total_clients_income_list):.2f}\n" \
                 f"Granted Loans: {count_granted_loans_count}, Total Sum: {total_granted_to_clients_amount:.2f}\n" \
                 f"Available Loans: {len(self.loans)}, Total Sum: {sum(total_not_granted_list):.2f}\nAverage Client Interest Rate: {avg_client_interest_rate:.2f}"

        return result
