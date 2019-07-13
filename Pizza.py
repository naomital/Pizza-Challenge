import importlib
import sys
import csv


class Pizza:
    def getDescription(self):
        return self.__class__.__name__
    def getTotalCost(self):
        return self.__class__.cost

class TakeAway(Pizza):
    cost = 0.0

class Decorator(Pizza):
    def __init__(self, pizzaE):
        self.component = pizzaE
    def getTotalCost(self):
        return self.component.getTotalCost() + \
               Pizza.getTotalCost(self)
    def getDescription(self):
        return self.component.getDescription() + \
          ' ' + Pizza.getDescription(self)

class dough(Decorator):
    cost = 0.75
    def __init__(self, pizzaE):
        Decorator.__init__(self, pizzaE)

class cheese(Decorator):
    cost = 0.5
    def __init__(self, pizzaE):
        Decorator.__init__(self, pizzaE)

class ExtraCheese(Decorator):
    cost = 0.25
    def __init__(self, pizzaE):
        Decorator.__init__(self, pizzaE)

class TomatoSauce(Decorator):
    cost = 0.25
    def __init__(self, pizzaE):
        Decorator.__init__(self, pizzaE)

class olives(Decorator):
    cost = 0.2
    def __init__(self, pizzaE):
        Decorator.__init__(self, pizzaE)

class Chocolate(Decorator):
    cost = 0.2
    def __init__(self, pizzaE):
        Decorator.__init__(self, pizzaE)

class Mushrooms(Decorator):
    cost = 0.2
    def __init__(self, pizzaE):
        Decorator.__init__(self, pizzaE)

class Onion(Decorator):
    cost = 0.2
    def __init__(self, pizzaE):
        Decorator.__init__(self, pizzaE)

class SweetPotato(Decorator):
    cost = 0.2
    def __init__(self, pizzaE):
        Decorator.__init__(self, pizzaE)


def orders():
    libClasses ={
"1" : dough,
"2" : TomatoSauce,
"3" : cheese,
"4" : ExtraCheese,
"5" : olives,
"6" : Chocolate,
"7" : Mushrooms,
"8" : Onion,
"9" : SweetPotato
                 }
    print(" ~~~~~~~~~~~~~~~~~~~~~~~ ")
    print("|    Italian Takeway    |")
    print("|    Ordering System    |")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~ ")
    print("")
    print("Welcome to our takeway ordering system.")

    code = input("Enter the option Pizza toppings you would like to order: (e.g.1)")
    order = TakeAway()

    while code != 'X':
        file = open("food-menu.txt", "r")
        for line in file:
            data = line.split(":")
            itemCode = data[0]
            itemName = data[1]
            if code == itemCode:

                order = libClasses[itemCode](order)

        file.close()
        code = input("Enter  another option Pizza toppings or X to go next: (e.g.1)")
    pizza1 = dough(order)
    print("you order: ", end="")
    print(pizza1.getDescription().strip())
    print("$", pizza1.getTotalCost())
    print("To pay Press 1 to cancel press 2:")
    name = input("Enter your name:")
    id = input("Enter ID number:")
    Ticket = input("Enter Ticket Number:")
    back = input("Enter Three digits on back of card")


    with open('Orders_file.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow([name, id, Ticket, back, pizza1.getDescription().strip(), pizza1.getTotalCost() ])

if __name__ == "__main__":
    orders()
    # pizza1 = dough(ExtraCheese(SweetPotato(TakeAway())))
    # print(pizza1.getDescription().strip() +
    #       ": $" + str(pizza1.getTotalCost()))
    # pizza2 = dough(TomatoSauce(Chocolate(
    # SweetPotato(cheese()))))
    #
    # print(pizza2.getDescription().strip() +
    #  ": $" + str(pizza2.getTotalCost()))
