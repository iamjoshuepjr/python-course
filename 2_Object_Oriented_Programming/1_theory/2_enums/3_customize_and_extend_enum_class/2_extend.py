# ==========================================================================
#                       Extend Python enum classes
# ==========================================================================
# Python doesn't allow you to extend an enum class unless it has no member. 
# However, this is not limitation. Because you can define a base class that has 
# methods but no members and then extend this base class.

from enum import Enum
from functools import total_ordering

@total_ordering
class OrderedEnum(Enum):
    def __lt__(self, other):
        if isinstance(other, OrderedEnum):
            return self.value < other.value
        return NotImplemented

class ApprovalStatus(OrderedEnum):
    PENDING = 1
    IN_PROGRESS = 2
    APPROVED = 3

status = ApprovalStatus(2)
if status < ApprovalStatus.APPROVED:
    print('The request has not been approved.')
