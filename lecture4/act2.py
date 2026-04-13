# Profit loss
from colorama import Fore, init
init(autoreset=True)

buying_cost = float(input("Enter the buying cost: "))
selling_cost = float(input("Enter the selling cost: "))

if selling_cost > buying_cost:
    profit = selling_cost - buying_cost
    print(Fore.Green + f"you made a profit of {profit:.2f}")
else:
    loss = buying_cost - selling_cost
    print(Fore.RED + f"you incurred a loss of {loss:.2f}" )
