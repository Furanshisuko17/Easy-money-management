import os


class Expense:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system('cl')    


def print_all(expense_list):
    for expense in expense_list:
        print("Nombre\t\t|\tdinero")
        print(expense.name, "\t\t|\t", expense.amount, sep='')
    

expense_list = []

finished = False

clear_console()

while not finished:

    print_all(expense_list)

    name = input("Ingrese el nombre del gasto: ")
    clear_console()
    amount = input("Ingrese la cantidad de dinero: ")
    clear_console()
    
    expense_list.append(Expense(name, amount))
