from classes.Keyboard import Keyboard
from classes.Monitor import Monitor
from classes.Mouse import Mouse
from classes.Computer import Computer

class Order:
    order_counter =  0
    def __init__(self, computer):
        Order.order_counter += 1
        self.__id_order = Order.order_counter
        self.__computer = computer
    
    @property
    def id_order(self):
        return self.__id_order
    
    @id_order.setter
    def id_order(self, id_order):
        self.__id_order = id_order
    
    @property
    def computer(self):
        return self.__computer

    def add_computer(self, computer):
        self.__computer.append(computer)

    def __str__(self) -> str:
        str_computer = ''
        for computer in self.__computer:
            str_computer += computer.__str__()
        
        return f"""
               Order: {self.id_order}
               Computers: {str_computer}
               """
if __name__ == '__main__':
    keyboard1 = Keyboard('HP', 'USB')
    mouse1 = Mouse('Acer', 'Bluetooth')
    monitor1 = Monitor('HP', 45)
    computer1 = Computer('Asus', monitor1, keyboard1, mouse1)
    print(computer1)