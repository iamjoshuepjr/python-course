from classes.InputDevice import InputDevice

class Mouse(InputDevice):
    mouse_counter = 0
    
    def __init__(self, brand, input_type):
        Mouse.mouse_counter += 1
        self.__id_mouse = Mouse.mouse_counter
        super().__init__(brand, input_type)
        
    def __str__(self):
        return f"Mouse ID: {self.__id_mouse} - Mouse Brand: {self.brand} - Mouse Input Type: {self.input_type}"
        
if __name__ == '__main__':
    mouse1 = Mouse('HP', 'Bluetooth')
    print(mouse1)

    mouse2 = Mouse('Acer', 'Bluetooth')
    print(mouse2)