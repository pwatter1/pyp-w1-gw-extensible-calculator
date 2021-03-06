from datetime import datetime

from calculator.operations import *
from calculator.exceptions import *


def create_new_calculator(operations=None):
    """
    Creates a configuration dict for a new calculator. Optionally pre loads an
    initial set of operations. By default a calculator with no operations
    is created.

    :param operations: Dict with initial operations.
                       ie: {'sum': sum_function, ...}
    """
    calc = {
        'operations': {},
        'history': []
        }
    
    if operations != None:
        calc["operations"] = operations
        
    return calc
        

def perform_operation(calc, operation, params):
    """
    Executes given operation with given params. It returns the result of the
    operation execution.

    :param calc: A calculator.
    :param operation: String with the operation name. ie: 'add'
    :param params: Tuple containing the list of nums to operate with.
                   ie: (1, 2, 3, 4.5, -2)
    """
    for entry in params:
        if type(entry) == int or type(entry) == float:
            continue
        else:
            raise InvalidParams('Given params are invalid.')
            
    if calc['operations'].get(operation) == None:
        raise InvalidOperation('Given operation is invalid.')

    function = calc["operations"][operation]
    
    calc['history'].append((datetime.now().strftime('%Y-%m-%d %H:%M:%S'), operation, params, function(*params)))
    
    return function(*params)


def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    square_root = lambda ...
    add_new_operation(calc, operation={'square_root': square_root})
    """
    
    if type(operation) != dict:
        raise InvalidOperation('Given operation is invalid.')
    
    calc['operations'] = operation
    


def get_operations(calc):
    """
    Returns the list of operation names supported by given calculator.
    """
    return list(calc['operations'].keys())


def get_history(calc):
    """
    Returns the history of the executed operations since the last reset or
    since the calculator creation.

    History items must have the following format:
        (:execution_time, :operation_name, :params, :result)

        ie:
        ('2016-05-20 12:00:00', 'add', (1, 2), 3),
    """
    
    return calc['history']


def reset_history(calc):
    """
    Resets the calculator history back to an empty list.
    """
    calc['history'] = []


def repeat_last_operation(calc):
    """
    Returns the result of the last operation executed in the history.
    """
    if calc['history'] == []:
        return None
    return calc['history'][-1][3]
