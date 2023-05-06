from enum import Enum 

class PaymentSatus(Enum):
    PENDING = 1
    COMPLETED = 2
    REFUNDED = 3

    # To customize how the PaymentStatus member's 
    # is represented in the string, you can implement 
    # the __str__ method. 

    def __str__(self):
        return f'{self.name.lower()}({self.value})'
    
    # implementing __eq__ method 
    # To allow the comparation between PaymentStatus member and an integer

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        
        if isinstance(other, PaymentSatus):
            return self is other 
        
        return False 

print(PaymentSatus.PENDING)

if(PaymentSatus.PENDING == 1):
    print('The payment is pending.')