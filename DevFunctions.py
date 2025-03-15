def AlertPrint(message: str, type: str) -> None:
    """
    Prints alert messages Easly

    >>> error
    >>> info
    >>> test

    :Exemple:
    >>> Alert_Print('hello !', 'info')
    >>> output : INFO # hello !
    """

    if type == 'error':
        print(f'\033[31mERROR # \033[0m{message}')

    elif type == 'info':
        print(f'\033[32mINFO # \033[0m{message}')

    elif type == 'test':
        print(f'\033[35mTEST # \033[0m{message}')

    else:
        print(f'\033[31mERROR # \033[0mINVALID ALERT TYPE !')