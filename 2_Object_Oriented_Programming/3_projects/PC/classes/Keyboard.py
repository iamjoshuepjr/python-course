from classes.InputDevice import InputDevice

class Keyboard(InputDevice):
    keyboard_counter = 0
    
    def __init__(self, brand, input_type):
        Keyboard.keyboard_counter += 1
        self.__id_keyboard = Keyboard.keyboard_counter
        super().__init__(brand, input_type)
        
    def __str__(self):
        return f"Keyboard ID: {self.__id_keyboard} - Keyboard Brand: {self.brand} - Keyboard Input Type: {self.input_type}"

if __name__ == '__main__':
    keyboard1 = Keyboard('HP', 'Bluetooth')
    print(keyboard1)

    keyboard2 = Keyboard('HP', 'Bluetooth')
    print(keyboard2)