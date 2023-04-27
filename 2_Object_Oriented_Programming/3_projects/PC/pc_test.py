from classes.Computer  import Computer
from classes.Keyboard  import Keyboard
from classes.Monitor   import Monitor
from classes.Mouse     import Mouse
from classes.Order     import Order

keyboard = Keyboard('HP', 'Bluetooth')
mouse  = Mouse('Samsung', 'Bluetooth')
monitor = Monitor('Acer', 34)
computer = Computer('HP', monitor, keyboard, mouse)

keyboard2 = Keyboard('HP', 'Bluetooth')
mouse2  = Mouse('Samsung', 'Bluetooth')
monitor2 = Monitor('Acer', 34)
computer2 = Computer('HP', monitor2, keyboard2, mouse2)

keyboard3 = Keyboard('Gamer', 'Bluetooth')
mouse3 = Mouse('Gamer', 'Bluetooth')
monitor3 = Monitor('Gamer', 45)
computer3 = Computer('Gamer', keyboard3, mouse3, monitor3)

computer_list = [computer, computer2]

order1 = Order(computer_list)
order1.add_computer(computer3)
print(order1)