import csv
import sys,subprocess


class ecart:
    instances = []
    cart = []
    price = 0
    def __init__(self,item,cost):
        self.item = item
        self.cost = cost
        ecart.instances.append(self)
        
    def add_item(self):
        if not self.item in ecart.cart:
            ecart.cart.append(self.item)
            ecart.price += self.cost
        else:
            print("""
prompt:
================================
ITEM ALREADY EXISTED IN YOUR CART
================================
        """)
            
        
    def remove_item(self):
        if self.item in ecart.cart:
            ecart.cart.remove(self.item)
            ecart.price -= self.cost
        else:
            print("""
prompt:
================================
ITEM DOSENT EXIST IN YOUR CART
================================
        """)
            
        
    def checkout(self):
        print("You bought:")
        for items in ecart.cart:
            print(f'===> {items}')
        print(f'your total bill is {ecart.price}')
        pay = int(input("enter amount to pay == > $"))
        if pay == ecart.price:
            print("\n°°°THANKS FOR SHOPPING WITH US °°°")
            input("TYPE ANYTHING TO GO TO MENU:")
            subprocess.run('clear')
            main()
        elif pay < ecart.price:
            print("insufficient amount")
        elif pay > ecart.price:
            print(f"HERE IS YOUR CHANGE: ${pay-ecart.price}")
            print("\n=====°°°THANKS FOR SHOPPING WITH US°°°=====")
            input("TYPE ANYTHING TO GO TO MENU:")
            subprocess.run('clear')
            main()
        else:
            print("invalid input")
            
               
    @classmethod
    def instantiate_from_csv(cls):
        with open("data.csv","r") as t:
            reader = csv.DictReader(t)
            items = list(reader)
            for instance in items:
                ecart(item = instance.get("item"),cost = int(instance.get("cost")))
                
ecart.instantiate_from_csv()



print("========WELCOME TO ECART========")
def menu1():
    print("____|MENU|____")
    print("1.SHOP")
    print("2.QUIT")
    print("3.CREDITS")
        
        
def menu1_res():
    res = int(input(">>>"))
    return res
        
        
def menu2():
    print("Please type number to add items to cart")
    num = 0
    for items in ecart.instances:
        print(f"{num}.{items.item}===>{items.cost}")
        num += 1
    print("==MISLANIOUS OPERATIONS==")
    print(f"{len(ecart.instances)}.Back")
    print(f"{len(ecart.instances)+1}.Remove item")
    print(f"{len(ecart.instances)+2}.Checkout")
        
        
def menu2_res():
    res = int(input("\n>>>ENTER ITEM NO:"))
    return res


def func():
    while True:
        y = menu2_res()
        if y < len(ecart.instances):
            
            print("""
 |===========|
 | YOUR CART |
 |===========|
            """)
            print(ecart.cart)
            subprocess.run("clear")
            menu2()
            ecart.instances[y].add_item()
            print("""
 |===========|
 | YOUR CART |
 |===========|
            """)
            print(ecart.cart)
        elif y == len(ecart.instances)+1:
            inp = int(input("ENTER ITEM NO TO REMOVE: "))
            subprocess.run("clear")
            menu2()
            ecart.instances[inp].remove_item()
            print("""
 |===========|
 | YOUR CART |
 |===========|
            """)
            print(ecart.cart)
        elif y == len(ecart.instances):
            subprocess.run("clear")
            main()
        elif y == len(ecart.instances)+2:
            subprocess.run("clear")
            ecart.instances[0].checkout()
            break
        else:
            print("please enter valid number")


def credits():
    print("""
======================================
INSTAGRAM: dyne_esty

LINK:https://instagram.com/dyne_esty?igshid=ZDdkNTZiNTM=


YOUTUBE: Dynesty

LINK:https://youtube.com/@dynesty718    
======================================
""")
    input("TYPE ANY THING TO GO BACK:")
    subprocess.run("clear")
    main()         
def main():
        ecart.cart.clear()
        menu1()
        x = menu1_res()
        if x == 1:
            subprocess.run("clear")
            menu2()
            func()
        elif x == 2:
            print("THANKS FOR VISITING OUR STORE")
        elif x == 3:
            subprocess.run("clear")
            credits()
main()    