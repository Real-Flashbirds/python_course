from typing import List

from logger import logger


def check_validity_arg1(func: callable) -> callable:
    """
    the decorator calling function
    :param func: The decorated function, given as an argument
    :return: the wrapper function, to be used as decorator
    """

    def arg_checker(arg1: List[float], **kwargs):
        # first, call the boilerplate junk to test validity of arg1
        # ....wrapper function begins here....
        if not isinstance(arg1, list):
            logger.error('arg1 is not a list')
            raise TypeError('arg1 is not a list')
        for item in arg1:
            if not isinstance(item, float):
                logger.error(f'item {item} is not a float')
                raise TypeError(f'item {item} is not a float')

        # now call the decorated function and return its value
        return func(arg1, **kwargs)
        # .... wrapper function ends here ....

    # now, return the wrapper to be used as a wrapper function in the decorator.
    return arg_checker


@check_validity_arg1
def nice_def(arg1: List[float], **kwargs) -> bool:
    """
    example of boilerplate arg checking
    :param arg1: First argument is a list of floats
    :result: True if arg1 complies with the type rules
    """
    return True