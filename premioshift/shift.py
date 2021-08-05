from .shifter import shift_message

class Shift:
    """
    A Shift is a object that contains all information to encrypt or decrypt a message.
    """
    def __init__(self, **kwargs):
        self.message = kwargs.get("message", "")
        self.key = kwargs.get("key", "")
        self.position = kwargs.get("cur_pos", 0)

    """
    Sets a new message.

    Arguments:
        message (str): The new message to this Shift
    """
    def set_message(self, message: str, pos: int = 0):
        self.message = message
        self.position = pos

    """
    Sets a new key.

    Arguments:
        key (str): The new key to this Shift
    """
    def set_key(self, key: str):
        self.key = key

    """
    Returns the message shifted by a specific value

    Arguments:
        shift (int): The total steps to shift
    
    kwargs:
        dont_save (bool): Save the new message and new position

    Return:
        str: The final message
    """
    def shift(self, shift: int, **kwargs) -> str:
        dont_save = kwargs.get("dont_save", False)

        new_message = shift_message(message=self.message, key=self.message, shift=shift)

        if not dont_save:
            self.message = new_message
            self.position = self.position + shift

        return new_message