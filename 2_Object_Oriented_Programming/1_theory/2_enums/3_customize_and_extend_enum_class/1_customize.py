from enum import Enum 
from functools import total_ordering

@total_ordering
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
    
    # implementing __lt__ method 
    # To allow the sorting base on their value 

    def __lt__(self, other):
        if isinstance(other, int):
            return self.value < other
        
        if isinstance(other, PaymentSatus):
            return self.value <  other.value
        
        return False
    
    # implementing __bool__ method
    def __bool__(self):
        if self is self.COMPLETED:
            return True
        
        return False

# compare with an integer
status = 1
if status < PaymentSatus.COMPLETED:
    print('The payment has not completed!')

# compare with another member
status = PaymentSatus.PENDING
if status >= PaymentSatus.COMPLETED:
    print('The payment is not pending.')

for member in PaymentSatus:
    print(member, bool(member))