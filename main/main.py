import itertools
import os
from tabulate import tabulate

class Expense:

    id = itertools.count()

    def __init__(self, name, amount: float):
        self.instance_id = next(Expense.id)
        self.name = name
        self.amount = amount

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)    

def print_all(expense_list):    
    sum = 0.0
    print_list = []
    
    for expense in expense_list:
        sum += expense.amount
        print_list.append([(expense.instance_id+1), expense.name, expense.amount])
        
        # print((expense.instance_id+1), "\t|", expense.name, "\t\t\t|", expense.amount, sep='')
        
    print(tabulate(print_list, headers = ["ID", "Nombre", "Dinero"]))
    print("_______________________________________")
    print("\t\t\tTotal: S/.", "{:.2f}".format(sum), sep='')  
    print(" ")

clear_console()
        
expense_list = []
finished = False

while not finished:

    print_all(expense_list)

    name = input("Ingrese el nombre del gasto: ")
    clear_console()

    print_all(expense_list)
    
    while True:    
        try:
            print(name, ': S/.', sep='', end='')
            amount = float(input())
            break
        except ValueError:
            
            print("Ingrese un número.")
        
    clear_console()
    
    expense_list.append(Expense(name, amount))
