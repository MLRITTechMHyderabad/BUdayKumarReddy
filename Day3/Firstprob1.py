from abc import ABC,abstractmethod
class chai(ABC):
    def __init__(self,name,base_price,quantity_in_stock):
        self.name=name
        self.base_price=base_price
        self.quantity_in_stock=quantity_in_stock
    @abstractmethod
    def calculate_price(self):
        pass 
    @abstractmethod     
    def display_info(self):
        pass   
class Masalchai(chai):
    
    def calculate_price(self):
        self.base_price+=10

    def display_info(self):
        price=self.calculate_price()
        print("Name:{self.name} | price for cup :{self.price} | Quantity in stock :{self.quantity_in_stock}")

class GInger_chai(chai):
    def calculate_price(self):
        self.base_price+=8

    def display_info(self):
        price=self.calculate_price()
        print("Name:{self.name} | price for cup :{self.price} | Quantity in stock :{self.quantity_in_stock}")   
class Elachichai(chai):
    def calculate_price(self):
        self.base_price+=10

    def display_info(self):
        price=self.calculate_price()
        print("Name:{self.name} | price for cup :{self.price} | Quantity in stock :{self.quantity_in_stock}")
class ChaiInventory:
    def __init__(self):
        self.inventory=[]
    def add_chai(self,chai_obj):
        self.inventory.append(chai_obj)    

    def show_inventory(self):
        for chai in self.inventory:
            chai.display_info()
    def get_total_inventory_value(self):
        total=0
        for chai in self.inventory:
            total+=chai.calculate_price()*chai.quantity_in_stock
        return total    
inventory=ChaiInventory()
chai1=Masalchai("Masala",10,10)
chai2=GInger_chai("ginger",10,8)
chai3=Elachichai("elachi",10,12)
inventory.add_chai(chai1)
inventory.add_chai(chai2)
inventory.add_chai(chai3)
inventory.show_inventory()
print("total inventory vakue :$",inventory.get_total_inventory_value())