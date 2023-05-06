from enum import Enum

class ResponseStatus(Enum):
    # in progress
    IN_PROGRESS = 1
    REQUESTIN = 1
    PENDING = 1

    # success
    SUCESS = 2
    OK = 2
    FULFILLED = 2

    # error
    ERROR = 3
    NOT_OK = 3
    REJECTED = 3

code = 'OK'
if ResponseStatus[code] is ResponseStatus.SUCESS:
    print('The request completed successfully.')