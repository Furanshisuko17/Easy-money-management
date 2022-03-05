import os

class Expense:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)    

def print_all(expense_list):    
    sum = 0
    print("Nombre:\t\t|Dinero:")
    
    for expense in expense_list:
        sum += expense.amount
        print(expense.name, "\t\t|", expense.amount, sep='')

    print("_______________________________")
    print("\t\tTotal: ", sum, sep='')  
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
            amount = int(input("Ingrese la cantidad de dinero: "))
            break
        except ValueError:
            print("Ingrese un número.")
        
    clear_console()
    
    expense_list.append(Expense(name, amount))
