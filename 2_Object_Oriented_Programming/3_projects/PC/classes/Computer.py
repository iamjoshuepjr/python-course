# from Keyboard import Keyboard
# from Monitor import Monitor
# from Mouse import Mouse

class Computer:
    computer_counter = 0
    def __init__(self, name, monitor, keyboard, mouse):
        Computer.computer_counter += 1
        self.__id_computer = Computer.computer_counter
        self.__name = name 
        self.__monitor = monitor
        self.__keyboard = keyboard
        self.__mouse = mouse
    
    @property
    def id_computer(self):
        return self.__id_computer
    
    @id_computer.setter
    def id_computer(self, id_computer):
        self.__id_computer = id_computer
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def id_name(self, name):
        self.__name = name

    @property
    def monitor(self):
        return self.__monitor

    @monitor.setter
    def monitor(self, monitor):
        self.__monitor = monitor

    @property
    def keyboard(self):
        return self.__keyboard  

    @keyboard.setter
    def keyboard(self, keyboard):
        self.__keyboard = keyboard 
    
    @property
    def mouse(self):
        return self.__mouse

    @mouse.setter
    def mouse(self, mouse):
        self.__mouse = mouse

    def __str__(self) -> str:
        return f"""
        {self.name}: {self.id_computer}
        Monitor: {self.monitor}
        Keyboard: {self.keyboard}
        Mouse: {self.mouse}
        """
