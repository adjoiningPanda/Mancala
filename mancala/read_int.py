__author__ = 'robby'

def read_int(message, error_message):
    """
    Utility function to read integers from the command line.
    :param message: Message to output to tell what type of input to expect
    :param error_message: Error message to display when input is not an integer
    :return: Input as an integer
    """
    integer = ''
    while not integer:
        try:
            integer = int(raw_input(message))
        except ValueError:
            print(error_message)

    print

    return integer