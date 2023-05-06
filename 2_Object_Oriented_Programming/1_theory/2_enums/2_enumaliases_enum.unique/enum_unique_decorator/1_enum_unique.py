# =====================================================
# To define an enumeration with no aliases, 
# you can carefully use unique values for the members.
# =====================================================
import enum
from enum import Enum 

# =============================================================================
# To ensure an enumeration has no alias, you can use the enum.unique decorator. 
# Python will throw an exception if the enumeration has aliases.
# =============================================================================

@enum.unique
class Day(Enum):
    MON = 'Monday'
    TUE = 'Tuesday'
    WED = 'Wednesday'
    THU = 'Thursday'
    FRI = 'Friday'
    SAT = 'Saturday'
    SUN = 'Sunday'